from flask import jsonify, request, Blueprint
from ..crud.submissions import register_submission

def init(app):
    bp = Blueprint('submissions', __name__)

    @bp.route('/register_submission', methods=['POST'])
    def register():
        return register_submission()

    app.register_blueprint(bp, url_prefix="/api/v1")
g
