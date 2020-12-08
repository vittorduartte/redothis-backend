from flask import jsonify, request, Blueprint
from ..crud.course import register_course, get_all_courses, get_course_by_id

def init(app):

    bp = Blueprint('courses', __name__)

    @bp.route('/get_courses', methods=['GET'])
    def get_courses():
        return get_all_courses()

    @bp.route('/get_course', methods=['GET'])
    def get_course():
        return get_course_by_id()
    
    app.register_blueprint(bp, url_prefix="/api/v1")
