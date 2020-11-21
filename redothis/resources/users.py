from flask import jsonify, request
from ..crud.users import register_user, auth_user

def init(app):
    @app.route('/hello')
    def hello():
        return jsonify({'message':'Hello class!'}), 200

    @app.route('/user', methods=['POST'])
    def register():
        return register_user()

    @app.route('/auth', methods=['POST'])
    def auth():
        return auth_user()

