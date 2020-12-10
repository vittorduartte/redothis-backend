from flask import request, jsonify, Blueprint
from ..crud.degree import register_degree, get_all_degrees, get_degree_by_id
import os 

def init(app):

    bp = Blueprint('degrees', __name__)

    @bp.route('/degree', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_degree()
        else:
            return get_degree_by_id()

    @bp.route('/degrees', methods=['GET'])
    def get_degree():
        return get_all_degrees()
    
    app.register_blueprint(bp, url_prefix=os.environ.get('URL_PREFIX'))
