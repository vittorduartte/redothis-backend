from flask import jsonify, request, Blueprint
from ..crud.knowledge_areas import register_knowledge_area, get_knowledge_area_by_id, get_all_knowledge_areas

def init(app):
    bp = Blueprint('knowledge_areas', __name__)

    @bp.route('/area', methods=['GET', 'POST'])
    def get_areas():
        if request.method == 'POST':
            return register_knowledge_area()
        else:
            return get_knowledge_area_by_id()

    @bp.route('/areas', methods=['GET'])
    def get_area():
        return get_all_knowledge_areas()

    app.register_blueprint(bp, url_prefix="/api/v1")

