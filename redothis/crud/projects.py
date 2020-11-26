from flask import request, jsonify
from ..extensions.database import database as db
from ..models import Project, Author, project_schema, project_schemas

def register_project():
    title = request.json['title']
    subttle = request.json['subtitle']
    category = request.json['category']
    knowledge_area = request.json['knowledge_area']
    student = request.json['student']
    tutor = request.json['tutor']

    project = Project(title, subtitle, category, knowledge_area)
    db.session.add(project)

    student_in_process = Project.query.filter_by(id=project.id).first()

    if(student_in_process):
        return jsonify({'message':'user already working', 'data':False}), 200
    else:
        student_author = Author(student, project.id)
        tutor_author = Author(tutor, project_id)
        try:
            db.session.add(student_author)
            db.session.add(tutor_author)
            db.commit()
            return jsonify(project_schema.dump(project)), 201
        except:
            return jsonify({'message':'error on transaction', 'data':False}), 200
