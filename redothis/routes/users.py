from flask import jsonify, request
from ..crud import user


def init(app):
    
    @app.route('/helloclass')
    def hello():
        return jsonify({'message': 'Hello class!'})
    
    @app.route('/user', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            return user.post_user()
        else:
            return jsonify({'user': 'unknown'}), 200