from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions.database import database as db
from ..models import (
    User,
    user_schema,
    users_schema,
    Degree,
    Course
)


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


def get_students_by_course():
    course_id = request.args.get("course")
    type_user = 0 if request.args.get("type") == 'student' else 1
    course_users = User.query.filter_by(
        course_id=course_id, type_user=type_user)

    if course_users.first():
        return jsonify({'message': 'success', 'data': users_schema.dump(course_users)}), 200
    else:
        return jsonify({'message': 'users_not_exists', 'data': False}), 200


def auth_user():
    auth = request.authorization
    exists_user = User.query.filter_by(email=auth.username).first()

    if exists_user:
        if check_password_hash(exists_user.password, auth.password):
            user = User.query.join(Degree, User.degree_id == Degree.id).join(Course, User.course_id == Course.id).add_columns(
                Degree.name, Course.name, Course.id).filter(User.id == exists_user.id).first()
            dumped_data = user_schema.dump(user[0])
            dumped_data['degree'] = user[1]
            dumped_data['course'] = user[2]
            dumped_data['id_course'] = user[3]
            return jsonify({'message': 'success', 'data': dumped_data}), 200
        else:
            return jsonify({'message': 'wrong_password', 'data': False}), 200
    else:
        return jsonify({
            'message': 'user_not_exists', 'data': False
        }), 200


def get_user_by_id():
    user_id = request.args.get("id")

    user = User.query.join(Degree, User.degree_id == Degree.id).join(
        Course, User.course_id == Course.id).add_columns(Degree.name, Course.name).filter(User.id == user_id).first()

    if user:
        dumped_data = user_schema.dump(user[0])
        dumped_data['degree'] = user[1]
        dumped_data['course'] = user[2]
        dumped_data['type_user'] = "Estudante" if dumped_data['type_user'] == 0 else "Professor"

        return jsonify({'message': 'success', 'data': dumped_data}), 201
    else:
        return jsonify({'message': '_invalid_user_id__', 'data': False}), 200
