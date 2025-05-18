from . import api
from ..models import User, db, UserInGroup, Project
import jwt, os
from flask import Flask, jsonify, request, current_app, session
import datetime
import hashlib

def find_user(token):
    if not token:
        return -1
    payload = ""
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return -2
    except jwt.InvalidTokenError:
        return -3
    
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
            projects_json.append(Project.query.filter_by(ID = p.Project_ID))
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
        )
        new_project.Project_Percentage = 0
        db.session.add(new_project)
        db.session.commit()

        new_useringroup = UserInGroup(
            User_ID = user.ID,
            Project_ID = new_project.ID,
            Admin = True
        )

        db.session.add(new_useringroup)
        db.session.commit()

        return jsonify({'message': 'Project registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500
