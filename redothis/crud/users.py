from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..extensions.database import database as db
from ..models.users import User, user_schema, users_schema


def register_user():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    type_user = request.json['type_user']
    university = request.json['university']
    degree = request.json['degree']
    course = request.json['course']
    password_hash = generate_password_hash(password)
    
    user = User(email,
                password_hash,
                name,
                type_user,
                university,
                degree,
                course
                )
    
    exists_user = User.query.filter_by(email=email).first()
    if exists_user:
        return jsonify({'message':'user already exists', 'data':{'email': False}}), 500

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': {'email': email}}), 201

    except:
        return jsonify({'message': 'unable to create', 'data':False}), 500
