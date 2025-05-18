from . import api
from ..models import User
from .. import db
import jwt, os
from flask import Flask, jsonify, current_app, request, session
import datetime
import hashlib

@api.route('/login', methods=['GET', 'POST'])
def login():      
    data = request.get_json()
    user = User.query.filter_by(Mail = data['usermail']).first()
    if user and user.verify_password(data['password']):
        extratime = datetime.timedelta(minutes=30)
        if(data['rememberme'] == 'Y'):
            extratime = datetime.timedelta(days=10)
        token = jwt.encode({
            'usermail': user.Mail,
            'exp': datetime.datetime.now() + extratime,
        }, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token,}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@api.route('/navdetail', methods=["GET"])
def isAuthenticated():

    token = request.headers.get("token")

    if not token:
        return jsonify({'authen': "false"}), 401
    payload = ""
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({'authen': "false"}), 401
    except jwt.InvalidTokenError:
        return jsonify({'authen': "false"}), 401
    
    user = User.query.filter_by(Mail = payload['usermail']).first()
        
    return jsonify({
        'authen': "true",
        'userID': user.ID,
        'username': user.Name
    }), 200

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not all(key in data for key in ('email', 'password', 'rePassword', 'name', 'terms')):
        return jsonify({'message': 'Missing data'}), 400

    if data['password'] != data['rePassword']:
        return jsonify({'message': 'Passwords do not match'}), 400

    try:
        new_user = User(
            Name=data['name'],
            Mail=data['email'],
        )
        new_user.password = data['password']
        new_user.Service_ID = 0
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500



       