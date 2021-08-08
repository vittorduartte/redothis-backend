import os
import datetime
import jwt
from flask import request
from flask import jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from werkzeug.security import safe_str_cmp
from ..extensions.database import database as db
from ..models.user import User
from ..models.user import user_schema
from ..models.user import users_schema
from ..models.course import Course
from ..models.degree import Degree


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
        return jsonify({'message': 'user already exists', 'data': {'email': False}}), 500

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': {'email': email}}), 201

    except:
        return jsonify({'message': 'unable to create', 'data': False}), 500


def get_students_by_course(id_course):
    course_users = User.query.filter_by(
        course_id=id_course, type_user=0)

    if course_users.first():
        return jsonify({'message': 'success', 'data': users_schema.dump(course_users)}), 200
    else:
        return jsonify({'message': 'users_not_exists', 'data': False}), 500


def authenticate(username, password):
    user = User.query.filter_by(email=username).first()
    if user and check_password_hash(user.password, password):
        return user


def indentity(payload):
    email = payload["username"]
    return user_schema.dump(User.query.add_columns(User.email, User.name, User.degree_id, User.course_id, User.type_user).filter_by(email=email).first())


def auth_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Could not verify", "WWW-Authenticate": "Basic auth='Login required'"}), 401

    exists_user = User.query.add_columns(User.email, User.password, User.name, User.degree_id, User.course_id, User.type_user).filter_by(email=auth.username).first()

    if exists_user:

        if check_password_hash(exists_user.password, auth.password):
            token = jwt.encode({"username": exists_user.email, 'exp': datetime.datetime.now(
            ) + datetime.timedelta(hours=12)}, os.getenv("SECRET_KEY"))

            return jsonify({'message': "User validated", 'data': user_schema.dump(exists_user), 'token': token.decode("UTF-8"), 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}), 200
        else:
            return jsonify({"message": "Could not verify", "WWW-Authenticate": "Basic auth='Login required'"}), 401

    else:
        return jsonify({
            'message': 'user_not_exists', 'data': False
        }), 500


def get_user_by_email(email):
    user = User.query.join(Degree, User.degree_id == Degree.id).join(
        Course, User.course_id == Course.id).add_columns(Degree.name, Course.name).filter(User.email == email).first()

    if user:
        dumped_data = user_schema.dump(user[0])
        dumped_data['degree'] = user[1]
        dumped_data['course'] = user[2]
        dumped_data['type_user'] = "Estudante" if dumped_data['type_user'] == 0 else "Professor"

        return jsonify({'message': 'success', 'data': dumped_data}), 201
    else:
        return jsonify({'message': 'invalid_user_id__', 'data': False}), 200
