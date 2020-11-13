from flask import request, jsonify
from werkzeug.security import generate_password_hash
from ..extensions.database import database
from ..models.users import Users, user_schema, users_schema


def register_user():
    print("\n\n\n\n"+request.args+"\n\n\n\n")
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    type_user = request.json['type_user']
    university = request.json['university']
    degree = request.json['degree']
    course = request.json['course']
    password_hash = generate_password_hash(password)
    user = User(email,
                password_hash,
                name,
                type_user,
                university,
                degree,
                course
                )

    try:
        print(password_hash)
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'resource created',
                        'data': result.data}), 201

    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500
