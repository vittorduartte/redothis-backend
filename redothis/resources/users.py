from flask import jsonify
from ..crud.users import register_user

def init(app):
    @app.route('/hello')
    def hello():
        return jsonify({'message':'Hello class!'}), 200

    @app.route('/user', methods=['POST'])
    def register():
        return register_user()
