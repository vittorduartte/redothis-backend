from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.projects import get_users_by_project
from ..controllers.projects import get_project_by_id
from ..controllers.projects import register_project
from ..controllers.submissions import get_project_submissions
from flask_jwt import jwt_required
from flask_jwt import current_identity


def init(app):
    bp = Blueprint('projects', __name__)

    @bp.route('/project', methods=['GET', 'POST'])
    @jwt_required()
    def register():
        if request.method == 'POST':
            return register_project()
        else:
            return get_project_by_id()

    @bp.route('/project/<int:id_project>/users', methods=['GET'])
    @jwt_required()
    def get_users_from_project(id_project):
        return get_users_by_project(id_project)

    @bp.route('/project/<int:id_project>/submissions', methods=['GET'])
    @jwt_required()
    def get_submissions_from_project(id_project):
        return get_project_submissions(id_project)

    @bp.route('/project/<int:id_project>/revisions', methods=['GET'])
    @jwt_required()
    def get_revisions_from_project(id_project):
        pass

    app.register_blueprint(bp, url_prefix="/api/v1")
