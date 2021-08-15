from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.users import get_students_by_course
from ..controllers.users import get_user_by_email
from ..controllers.users import register_user
from ..controllers.auth import auth_user
from ..controllers.projects import get_projects_by_user
from flask_jwt import jwt_required


def init(app):

    bp = Blueprint('users', __name__)

    @bp.route('/user', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            email = request.json['email']
            password = request.json['password']
            name = request.json['name']
            type_user = request.json['type_user']
            degree = request.json['degree']
            course = request.json['course']
            return register_user(email, password, name, type_user, degree, course)
        else:
            email = request.args.get('email')
            return get_user_by_email(email)

    @bp.route('/course/<int:id_course>/users', methods=['GET'])
    @jwt_required()
    def users_by_course(id_course):
        return get_students_by_course(id_course)

    @bp.route('/user/<int:id_usuario>/projects', methods=['GET'])
    @jwt_required()
    def get_projects_from_user(id_usuario):
        return get_projects_by_user(id_usuario)

    app.register_blueprint(bp, url_prefix="/api/v1")
