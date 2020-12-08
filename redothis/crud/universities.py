from flask import jsonify, request
from ..extensions.database import database as db
from ..models import University, university_schema, universitys_schema


def register_university():
    name = request.json['name']

    university = University(name)
    exists_university = University.query.filter_by(name=name).first()

    if exists_university:
        return jsonify({'message': 'university already exists', 'data': False}), 500

    try:
        db.session.add(university)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': university_schema.dump(university)}), 201
    except err:
        return jsonify({'message': err, 'data': False})


def get_all_universities():
    try:
        all_universities = University.query.order_by(University.name).all()
        return jsonify({'message': 'success', 'data': universitys_schema(all_universities)})
    except err:
        return jsonify({'message': err, 'data': False})
