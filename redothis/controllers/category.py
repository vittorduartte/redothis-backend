from flask import jsonify, request
from ..extensions.database import database as db
from ..models.category import Category
from ..models.category import category_schema
from ..models.category import categories_schema


def register_category(name):

    category = Category(name)

    exists_category = Category.query.filter_by(name=name).first()

    if exists_category:
        return jsonify({'message': 'category already exists', 'data': False}), 500

    try:
        db.session.add(category)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data': category_schema.dump(category)}), 201
    except:
        return jsonify({'message': 'error on transaction', 'data': False})


def get_all_categories():
    try:
        all_categories = Category.query.order_by(Category.name).all()
        return jsonify({'message': 'success',
                        'data': categories_schema.dump(all_categories)})
    except:
        return jsonify({'message': 'error on transaction', 'data': False})


def get_category_by_id(category_id):

    category = Category.query.filter_by(id=category_id).first()

    if category:
        return jsonify({'message': 'success', 'data': category_schema.dump(category)}), 200
    else:
        return jsonify({'message': '_invalid_category_id_', 'data': False}), 200
