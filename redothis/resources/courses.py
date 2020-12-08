from flask import jsonify, request, Blueprint
from ..crud.course import register_course, get_all_courses

def init(app):

    bp = Blueprint('courses', __name__)

    @bp.route('/get_courses', methods=['GET'])
    def get_courses():
        return get_all_courses()
    
    app.register_blueprint(bp, url_prefix="/api/v1")