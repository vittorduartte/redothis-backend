from flask import request, jsonify
from ..extensions.database import database as db
from ..models import Project, Author, project_schema, project_schemas

def register_project():
    title = request.json['title']
    subtitle = request.json['subtitle']
    category = request.json['category']
    knowledge_area = request.json['knowledge_area']
    student = request.json['student']
    tutor = request.json['tutor']

    project = Project(title, subtitle, category, knowledge_area, tutor)
    db.session.add(project)

    student_in_process = Author.query.filter_by(author_id=student).first()

    if(student_in_process):
        return jsonify({'message':'user already working', 'data':False}), 200
    else:
        student_author = Author(student, project.id)
        tutor_author = Author(tutor, project.id)
        try:
            db.session.add(student_author)
            db.session.add(tutor_author)
            db.session.commit()
            return jsonify(project_schema.dump(project)), 201
        except Exception as e:
            return jsonify({'message':'error on transaction', 'data':False}), 200

def get_user_projects():
    user_id = request.json['user_id']

    user_projects = Project.query.join(Author, Project.id == Author.project_id).filter(Author.author_id == user_id)

    if user_projects.first():
        return jsonify({'message': 'success', 'data': project_schemas.dump(user_projects)}), 200
    else:
        return jsonify({'message': 'users_not_exists', 'data': False}), 200
