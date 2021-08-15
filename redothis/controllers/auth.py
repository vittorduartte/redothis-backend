import datetime
import jwt
import os
from flask import request
from flask import jsonify
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from ..models.user import User
from ..models.user import user_schema
from ..models.user import users_schema


def authenticate(username, password):
    user = User.query.filter_by(email=username).first()
    if user and check_password_hash(user.password, password):
        return user


def indentity(payload):
    email = payload["username"]
    return user_schema.dump(User.query.add_columns(User.email, User.name, User.degree_id, User.course_id, User.type_user).filter_by(email=email).first())


def auth_user(auth):

    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Could not verify", "WWW-Authenticate": "Basic auth='Login required'"}), 401

    exists_user = User.query.add_columns(User.email, User.password, User.name, User.degree_id,
                                         User.course_id, User.type_user).filter_by(email=auth.username).first()

    if exists_user:

        if check_password_hash(exists_user.password, auth.password):
            token = jwt.encode({"username": exists_user.email, 'exp': datetime.datetime.now(
            ) + datetime.timedelta(hours=12)}, os.getenv("SECRET_KEY"))

            return jsonify({'message': "User validated", 'data': user_schema.dump(exists_user), 'token': token.decode("UTF-8"), 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)}), 200
        else:
            return jsonify({"message": "Could not verify", "WWW-Authenticate": "Basic auth='Login required'"}), 401

    else:
        return jsonify({
            'message': 'user_not_exists', 'data': False
        }), 500
