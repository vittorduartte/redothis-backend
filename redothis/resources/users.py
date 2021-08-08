from flask import jsonify
from flask import request
from flask import Blueprint
from ..controllers.users import get_students_by_course
from ..controllers.users import get_user_by_id
from ..controllers.users import register_user
from ..controllers.users import auth_user
from ..controllers.projects import get_projects_by_user
from flask_jwt import jwt_required


def init(app):

    bp = Blueprint('users', __name__)

    @bp.route('/oauth', methods=['POST'])
    def login():
        return auth_user()

    @bp.route('/user', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return register_user()
        else:
            return get_user_by_id()

    @bp.route('/course/<int:id_course>/users', methods=['GET'])
    @jwt_required()
    def users_by_course(id_course):
        return get_students_by_course(id_course)

    @bp.route('/user/<int:id_usuario>/projects', methods=['GET'])
    @jwt_required()
    def get_projects_from_user(id_usuario):
        return get_projects_by_user(id_usuario)

    app.register_blueprint(bp, url_prefix="/api/v1")
