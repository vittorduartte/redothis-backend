from flask import jsonify, request, Blueprint
from ..crud.submissions import register_submission, get_project_submissions, get_submission_by_id
from ..crud.revisions import get_submission_revisions


def init(app):
    bp = Blueprint('submissions', __name__)

    @bp.route('/submission', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_submission()
        else:
            return get_submission_by_id()

    @bp.route('/submission/<int:id_submission>/revisions', methods=['GET'])
    def get_revisions(id_submission):
        return get_submission_revisions(id_submission)

    app.register_blueprint(bp, url_prefix="/api/v1")
