from flask import Blueprint
from ..controllers.auth import auth_user


def init(app):

    bp = Blueprint('auth', __name__)

    @bp.route("/oauth", methods=['POST'])
    def auth():
        auth = request.authorization
        return auth_user(auth)

    app.register_blueprint(bp, url_prefix="/api/v1")
