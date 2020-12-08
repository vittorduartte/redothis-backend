from flask import jsonify, request, Blueprint
from ..crud.knowledge_areas import get_knowledge_area_by_id, get_all_knowledge_areas

def init(app):
    bp = Blueprint('knowledge_areas', __name__)

    @bp.route('/get_areas', methods=['GET'])
    def get_areas():
        return get_all_knowledge_areas()

    @bp.route('/get_area', methods=['GET'])
    def get_area():
        return get_knowledge_area_by_id()

    app.register_blueprint(bp, url_prefix="/api/v1")

