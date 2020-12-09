from flask import jsonify, request, Blueprint
from ..crud.projects import register_project, get_user_projects

def init(app):
    bp = Blueprint('projects', __name__)

    @bp.route('/project', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_project()
        else:
            return get_user_projects()
    
    app.register_blueprint(bp, url_prefix="/api/v1")
