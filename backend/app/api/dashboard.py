from . import api
from ..models import User, db, UserInGroup, Project, FinancialRecord
import jwt, os
from flask import Flask, jsonify, request, current_app, session
from datetime import datetime
import hashlib

def find_user(token):
    if not token:
        return -1
    payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    user = User.query.filter_by(Mail = payload['usermail']).first()
    return user

@api.route('/listprojects', methods=['GET'])
def listprojects():
    token = request.headers.get("token")
    user = find_user(token)

    if user:
        projects_json = []
        projects = UserInGroup.query.filter_by(User_ID=user.ID).all()
        for p in projects:
            projects_json.append(Project.query.filter_by(ID = p.Project_ID).first().to_json())
        return jsonify({'projects': projects_json}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@api.route('/createproject', methods=['POST'])
def createproject():
    token = request.headers.get("token")
    user = find_user(token)

    data = request.get_json()

    try:
        
        new_project = Project(
            Project_Name=data['Project_Name'],
            Description=data['Description'],
            Project_Budget=data['Project_Budget'],
            Project_Budget_Remaining=data['Project_Budget'],
            Project_Tags=data['Project_Tags'],
            Project_Deadline=datetime.strptime(data['Project_Deadline'], "%Y-%m-%d").date(),
            Custom_Status=data['Custom_Status'],
            Project_Percentage=data['Project_Percentage'],
        )
        db.session.add(new_project)
        db.session.commit()

        new_useringroup = UserInGroup(
            User_ID = user.ID,
            Project_ID = new_project.ID,
            Admin = 1
        )

        db.session.add(new_useringroup)
        db.session.commit()

        return jsonify({'message': 'Project registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500

@api.route('/project/<int:project_id>/', methods=['GET'])
def projectdet(project_id):
    token = request.headers.get("token")
    user = find_user(token)
    if user:
        projects_json = []
        project = UserInGroup.query.filter(UserInGroup.User_ID==user.ID, UserInGroup.Project_ID==project_id).first()
        if project:
            project = Project.query.filter_by(ID = project_id).first()
            return jsonify({"projectinfo": project.to_json()}), 200
        else:
            return jsonify({'error': 'Project not found'}), 404
    else:
        return jsonify({'error': 'Not Authenticated or Not Authorized or Project Does Not Exist'}), 404

        
@api.route('/listpeople/<int:project_id>/', methods=['GET'])
def listpeople(project_id):
    free = []
    al_as = []
    al_as2 =[]
    user_as = UserInGroup.query.filter_by(Project_ID=project_id).all()
    for u in user_as:
        al_as2.append(u.User_ID)
        al_as.append(User.query.filter_by(ID = u.User_ID).first().to_json())
    users = User.query.filter(~User.ID.in_(al_as2)).all()
    for t in users:
        free.append(t.to_json())

    return jsonify({"freepeople": free, "already_as": al_as}), 200

@api.route('/addassignee/', methods=['PUT'])
def addassignee():
    data = request.get_json()
    try:
        new_user = UserInGroup(
            User_ID=data['User_ID'],
            Project_ID=data['Project_ID'],
            Admin = True
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500

@api.route('/user_role/<int:project_id>/', methods=['GET'])
def user_role(project_id):
    try:
        token = request.headers.get("token")
        user = find_user(token)
        
        if user:
            project = UserInGroup.query.filter(UserInGroup.User_ID==user.ID, UserInGroup.Project_ID==project_id).first()
            return jsonify({"user_type": project.Admin}), 200
    except:
        return jsonify({'error': 'Not Authenticated or Not Authorized or Project Does Not Exist'}), 404

@api.route('/editproject/<int:project_id>/', methods=['POST'])
def editproject(project_id):
    try:
        token = request.headers.get("token")
        user = find_user(token)
        data = request.get_json()
        if user:
            project = Project.query.filter_by(ID=project_id).first()
            project.Project_Name = data['Project_Name']
            project.Project_Status = data['Project_Status']
            project.Project_Percentage = data['Project_Percentage']
            project.Custom_Status = data['Custom_Status']
            project.Project_Deadline = datetime.strptime(data['Project_Deadline'], "%Y-%m-%d").date()
            project.Project_Tags = data['Project_Tags']
            project.Description = data['Description']
            db.session.add(project)
            db.session.commit()
            return jsonify({'message': 'Project Edited successfully'}), 201
    except:
        return jsonify({'error': 'Not Authenticated or Not Authorized or Project Does Not Exist'}), 404
    
@api.route('/financialrecord/<int:project_id>/', methods=['POST'])
def financialrecord(project_id):
    try:
        token = request.headers.get("token")
        user = find_user(token)
        data = request.get_json()
        if user:
            project = Project.query.filter_by(ID=project_id).first()
            financialrecord = FinancialRecord()
            financialrecord.Project_ID = project_id
            financialrecord.Reason = data['Reason']
            financialrecord.Amount = data['Amount']
            if data["Type"] == "0":
                financialrecord.Expense = False
                project.Project_Budget = int(project.Project_Budget) + int(data["Amount"])
                project.Project_Budget_Remaining = int(project.Project_Budget_Remaining) + int(data["Amount"])
            elif data["Type"] == "1":
                financialrecord.Expense = True
                project.Project_Budget = int(project.Project_Budget)
                project.Project_Budget_Remaining = int(project.Project_Budget_Remaining) - int(data["Amount"])
            
            db.session.add(financialrecord)
            db.session.add(project)
            
            db.session.commit()
                
            return jsonify({'message': 'Finacial Recorded'}), 201
    except:
        return jsonify({'error': 'Not Authenticated or Not Authorized or Project Does Not Exist'}), 404