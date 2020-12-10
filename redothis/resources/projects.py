from flask import jsonify, request, Blueprint
from ..crud.projects import register_project, get_project_by_id, get_users_by_project
from ..crud.submissions import get_project_submissions


def init(app):
    bp = Blueprint('projects', __name__)

    @bp.route('/project', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_project()
        else:
            return get_project_by_id()

    @bp.route('/project/<int:id_project>/users', methods=['GET'])
    def get_users_from_project(id_project):
        return get_users_by_project(id_project)

    @bp.route('/project/<int:id_project>/submissions', methods=['GET'])
    def get_submissions_from_project(id_project):
        return get_project_submissions(id_project)

    @bp.route('/project<int:id_project>/revisions', methods=['GET'])
    def get_revisions_from_project(id_project):
        pass

    app.register_blueprint(bp, url_prefix="/api/v1")
