from flask import jsonify, request, Blueprint
from ..crud.universities import register_university, get_all_universities

def init(app):
     
     bp = Blueprint('universities', __name__)

     @bp.route('/universities', methods=['GET'])
     def get_all():
         return get_all_universities()
     
     app.register_blueprint(bp, url_prefix="/api/v1")