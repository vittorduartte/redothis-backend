from flask import request, jsonify, Blueprints

def init(app):
    bp = Blueprint('projects', __name__)

    app.register_blueprint(bp, url_prefix="/api/v1")