from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.knowledge_areas import get_all_knowledge_areas
from ..controllers.knowledge_areas import get_knowledge_area_by_id
from ..controllers.knowledge_areas import register_knowledge_area
from flask_jwt import jwt_required


def init(app):
    bp = Blueprint('knowledge_areas', __name__)

    @bp.route('/area', methods=['GET', 'POST'])
    @jwt_required()
    def get_areas():
        if request.method == 'POST':
            return register_knowledge_area()
        else:
            return get_knowledge_area_by_id()

    @bp.route('/areas', methods=['GET'])
    def get_area():
        return get_all_knowledge_areas()

    app.register_blueprint(bp, url_prefix="/api/v1")
