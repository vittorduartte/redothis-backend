from flask import request, jsonify, Blueprint
from ..crud.degree import register_degree, get_all_degrees, get_degree_by_id
import os 

def init(app):

    bp = Blueprint('degrees', __name__)

    @bp.route('/get_degrees', methods=['GET'])
    def get_degrees():
        return get_all_degrees()

    @bp.route('/get_degree', methods=['GET'])
    def get_degree():
        return get_degree_by_id()
    
    app.register_blueprint(bp, url_prefix=os.environ.get('URL_PREFIX'))
