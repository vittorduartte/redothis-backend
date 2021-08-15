from flask import jsonify, request
from ..extensions.database import database as db
from ..models.course import Course
from ..models.course import course_schema
from ..models.course import courses_schema


def register_course(name):

    course = Course(name)
    exists_course = Course.query.filter_by(name=name).first()

    if exists_course:
        return jsonify({'message': 'degree already exists', 'data': False}), 500

    try:
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': course_schema.dump(course)}), 201
    except:
        return jsonify({'message': 'Erro', 'data': False}), 500


def get_all_courses():
    try:
        all_courses_selected = Course.query.order_by(Course.name).all()
        return jsonify({'message': 'success',
                        'data': courses_schema.dump(all_courses_selected)}), 200
    except:
        return jsonify({'message': 'Erro', 'data': False}), 500


def get_course_by_id(course_id):

    course = Course.query.filter_by(id=course_id).first()

    if course:
        return jsonify({'message': 'success', 'data': course_schema.dump(course)}), 200
    else:
        return jsonify({'message': '_invalid_course_id_', 'data': False}), 500
