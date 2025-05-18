from . import api
from ..models import User, db
import jwt, os
from flask import Flask, jsonify, request, current_app, session
import datetime
import hashlib

def isowner(token, user):
    if not token:
        return -0
    payload = ""
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return 0
    except jwt.InvalidTokenError:
        return 0
    
    return "true" if (user == User.query.filter_by(Mail = payload['usermail']).first()) else ""

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

@api.route('/user/<int:user_id>/', methods=['GET'])
def get_user_profile(user_id):
    user = User.query.get(user_id)
    token = request.headers.get("token")
    if user:
        user_data = {
            'ID': user.ID,
            'Name': user.Name,
            'Mail': user.Mail,
            'Service_ID': user.Service_ID,
            'ProfilePIC': user.ProfilePIC,
            'About_Me': user.About_Me,
            'filename': hashlib.md5(str(user.Mail).encode('utf-8')).hexdigest(),
            'Date_Created': user.Date_Created, 
        }
        return jsonify({'userinfo': user_data, 'ownership': isowner(token, user)})
    else:
        return jsonify({'error': 'User not found'}), 404

@api.route('/uploadprofile', methods=['PUT'])
def uploadprofile():
    token = request.headers.get("token")
    user = find_user(token)

    if 'files' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['files']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if type(user) == type(1):
        return jsonify({'error': 'Not Authenticated properly'}), 400
    if file:        
        filename =  hashlib.md5(str(user.Mail).encode('utf-8')).hexdigest();
        file_type = file.filename.rsplit('.', 1)[1].lower()
        filename = os.path.join(current_app.config['UPLOAD_FOLDER'] + '/profilepics/', filename + "." + file_type)
        file.save(filename)
        user.ProfilePIC = file_type
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return jsonify({'error': 'An unknown error occured'}), 500
    