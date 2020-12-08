from flask import request, jsonify, Blueprint
from ..crud.degree import register_degree, get_all_degrees
import os 

def init(app):

    bp = Blueprint('degrees', __name__)

    @bp.route('/get_degrees', methods=['GET'])
    def get_degrees():
        return get_all_degrees()
    
    app.register_blueprint(bp, url_prefix=os.environ.get('URL_PREFIX'))