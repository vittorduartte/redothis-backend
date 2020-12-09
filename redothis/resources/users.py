from flask import jsonify, request, Blueprint
from ..crud.users import register_user, auth_user, get_students_by_course, get_user_by_id
from ..crud.projects import get_projects_by_user

def init(app):

    bp = Blueprint('users', __name__)

    @bp.route('/auth', methods=['POST'])
    def auth():
        return auth_user()

    @bp.route('/user', methods=['POST'])
    def register():
        return register_user()

    @bp.route('/users', methods=['GET'])
    def users_by_course():
        return get_students_by_course()

    @bp.route('/get_user', methods=['GET'])
    def get_user():
        return get_user_by_id()
    
    @bp.route('/user/<int:id_usuario>/projects', methods=['GET'])
    def get_projects_from_user(id_usuario):
        return get_projects_by_user(id_usuario) 

    
    app.register_blueprint(bp, url_prefix="/api/v1")


    

