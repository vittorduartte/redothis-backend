from flask import request
from flask import jsonify
from flask import Blueprint
from ..controllers.degree import get_all_degrees
from ..controllers.degree import get_degree_by_id
from ..controllers.degree import register_degree
from flask_jwt import jwt_required


def init(app):

    bp = Blueprint('degrees', __name__)

    @bp.route('/degree', methods=['GET', 'POST'])
    @jwt_required()
    def register():
        if request.method == 'POST':
            name = request.json['name']
            return register_degree(name)
        else:
            degree_id = request.args.get("id")
            return get_degree_by_id(degree_id)

    @bp.route('/degrees', methods=['GET'])
    def get_degree():
        return get_all_degrees()

    app.register_blueprint(bp, url_prefix="/api/v1")
