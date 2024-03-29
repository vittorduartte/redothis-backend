import os
import datetime
import jwt
from flask import request
from flask import jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from ..extensions.database import database as db
from ..models.user import User
from ..models.user import user_schema
from ..models.user import users_schema
from ..models.course import Course
from ..models.degree import Degree


def register_user(email, password, name, type_user, degree, course):
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
        return jsonify({'message': 'invalid_user_email', 'data': False}), 200
