from flask import jsonify, request, Blueprint
from ..crud.projects import register_project, get_user_projects

def init(app):
    bp = Blueprint('projects', __name__)

    @bp.route('/register_project', methods=['POST'])
    def register():
        return register_project()

    @bp.route('/get_projects', methods=['GET'])
    def get_projects():
        return get_user_projects()
    
    app.register_blueprint(bp, url_prefix="/api/v1")
