from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.revisions import get_submission_revisions
from ..controllers.revisions import get_revision_by_id
from ..controllers.revisions import register_revision
from flask_jwt import jwt_required


def init(app):
    bp = Blueprint('revisions', __name__)

    @bp.route('/revision', methods=['GET', 'POST'])
    @jwt_required()
    def register():
        if request.method == 'POST':
            submission_id = request.json['submission_id']
            create_by = request.json['user_id']
            comments = request.json['comments']
            attachment_filepath = request.json['attachment_filepath']
            return register_revision(submission_id, create_by, comments, attachment_filepath)
        else:
            revision_id = request.args.get('id')
            return get_revision_by_id(revision_id)

    app.register_blueprint(bp, url_prefix="/api/v1")
