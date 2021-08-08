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
            return register_revision()
        else:
            return get_revision_by_id()

    app.register_blueprint(bp, url_prefix="/api/v1")
