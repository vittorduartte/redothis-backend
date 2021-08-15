from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.course import get_all_courses
from ..controllers.course import get_course_by_id
from ..controllers.course import register_course
from flask_jwt import jwt_required


def init(app):

    bp = Blueprint('courses', __name__)

    @bp.route('/course', methods=['GET', 'POST'])
    @jwt_required()
    def register():

        if request.method == 'POST':
            name = request.json['name']
            return register_course(name)
        else:
            course_id = request.args.get('id')
            return get_course_by_id(course_id)

    @bp.route('/courses', methods=['GET'])
    def get_courses():
        return get_all_courses()

    app.register_blueprint(bp, url_prefix="/api/v1")
