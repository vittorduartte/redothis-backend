from flask import jsonify, request
from ..extensions.database import database as db
from ..models.degree import Degree
from ..models.degree import degree_schema
from ..models.degree import degrees_schema


def register_degree(name):

    degree = Degree(name)
    exists_degree = Degree.query.filter_by(name=name).first()

    if exists_degree:
        return jsonify({'message': 'degree already exists', 'data': False}), 500

    try:
        db.session.add(degree)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': degree_schema.dump(degree)}), 201
    except Exception as err:
        return jsonify({'message': err, 'data': False})


def get_all_degrees():
    try:
        all_degrees = Degree.query.order_by(Degree.name).all()
        return jsonify({'message': 'success', 'data': degrees_schema.dump(all_degrees)})
    except Exception as err:
        return jsonify({'message': err, 'data': False})


def get_degree_by_id(degree_id):

    degree = Degree.query.filter_by(id=degree_id).first()

    if degree:
        return jsonify({'message': 'success', 'data': degree_schema.dump(degree)}), 200
    else:
        return jsonify({'message': '_invalid_degree_id_', 'data': False}), 200
