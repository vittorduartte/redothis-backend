from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions.database import database as db
from ..models import User, user_schema, users_schema


def register_user():
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    type_user = request.json['type_user']
    degree = request.json['degree']
    course = request.json['course']
    password_hash = generate_password_hash(password)
    
    user = User(email,
                password_hash,
                name,
                type_user,
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

def get_students_by_course():
    course_id = request.json['course_id']
    course_users = User.query.filter_by(course_id=course_id)

    if course_users.first():
        return jsonify({'message': 'success', 'data': users_schema.dump(course_users)}), 200
    else:
        return jsonify({'message': 'users_not_exists', 'data': False}), 200

def auth_user():
    auth = request.authorization
    exists_user = User.query.filter_by(email=auth.username).first()

    if exists_user:
        if check_password_hash(exists_user.password, auth.password):
                return jsonify({'message': 'success', 'data': user_schema.dump(exists_user)}), 200
        else:
                return jsonify({'message': 'wrong_password', 'data': False}), 200
    else:
        return jsonify({
            'message': 'user_not_exists', 'data': False
        }), 200