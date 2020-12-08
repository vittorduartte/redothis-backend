from flask import jsonify, request
from ..extensions.database import database as db
from ..models import Course, course_schema, courses_schema


def register_course():
    name = request.json['name']
    university_id = request.json['university_id']

    course = Course(name, university_id)
    exists_course = Course.query.filter_by(name=name).first()

    if exists_course:
        return jsonify({'message': 'degree already exists', 'data': False}), 500

    try:
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': course_schema.dump(course)}), 201
    except:
        return jsonify({'message': 'Erro', 'data': False})


def get_all_courses():
    
    try:
        all_courses_selected = Course.query.order_by(Course.name).all()
        return jsonify({'message': 'success', 'data': courses_schema.dump(all_courses_selected)})
    except:
        return jsonify({'message': 'Erro', 'data': False})
