from flask import jsonify, request, Blueprint
from ..crud.users import register_user, auth_user, get_students_by_university_by_course  

def init(app):

    bp = Blueprint('users', __name__)

    @bp.route('/auth', methods=['POST'])
    def auth():
        return auth_user()

    @bp.route('/user', methods=['POST'])
    def register():
        return register_user()

    @bp.route('/university/users', methods=['GET'])
    def users_by_university_by_course():
        return get_students_by_university_by_course()
    
    app.register_blueprint(bp, url_prefix="/api/v1")


    

