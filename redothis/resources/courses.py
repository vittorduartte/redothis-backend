from flask import jsonify, request, Blueprint
from ..crud.course import register_course, get_all_courses, get_course_by_id

def init(app):

    bp = Blueprint('courses', __name__)

    @bp.route('/course', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_course()
        else:
            return get_course_by_id()

    @bp.route('/courses', methods=['GET'])
    def get_courses():
        return get_all_courses()
    
    app.register_blueprint(bp, url_prefix="/api/v1")
