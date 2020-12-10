from flask import jsonify, request, Blueprint
from ..crud.revisions import register_revision, get_submission_revisions, get_revision_by_id


def init(app):
    bp = Blueprint('revisions', __name__)

    @bp.route('/revision', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_revision()
        else:
            return get_revision_by_id()

    app.register_blueprint(bp, url_prefix="/api/v1")
