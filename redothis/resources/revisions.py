from flask import jsonify, request, Blueprint
from ..crud.revisions import register_revision, get_submission_revisions

def init(app):
    bp = Blueprint('revisions', __name__)

    @bp.route('/register_revision', methods=['POST'])
    def register():
        return register_revision()

    @bp.route('/get_revisions', methods=['GET'])
    def get_revisions():
        return get_submission_revisions()
    
    app.register_blueprint(bp, url_prefix="/api/v1")

