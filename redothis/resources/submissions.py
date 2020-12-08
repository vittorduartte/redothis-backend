from flask import jsonify, request, Blueprint
from ..crud.submissions import register_submission, get_project_submissions

def init(app):
    bp = Blueprint('submissions', __name__)

    @bp.route('/register_submission', methods=['POST'])
    def register():
        return register_submission()

    @bp.route('/get_submissions', methods=['GET'])
    def get_submissions():
        return get_project_submissions()

    app.register_blueprint(bp, url_prefix="/api/v1")

