from flask import request
from flask import jsonify
from flask import Blueprint
from ..controllers.category import get_all_categories
from ..controllers.category import get_category_by_id
from ..controllers.category import register_category
from flask_jwt import jwt_required


def init(app):
    bp = Blueprint('categories', __name__)

    @bp.route('/category', methods=['GET', 'POST'])
    @jwt_required()
    def register():
        if request.method == 'POST':
            return register_category()
        else:
            return get_category_by_id()

    @bp.route('/categories', methods=['GET'])
    @jwt_required()
    def get_categories():
        return get_all_categories()

    app.register_blueprint(bp, url_prefix="/api/v1")
