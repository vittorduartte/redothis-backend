from flask import request, jsonify
from ..extensions.database import database as db
from ..models import Project, User, Author, Category, KnowledgeArea, project_schema, project_schemas, users_schema

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

    user_projects = Project.query.join(Author, Project.id == Author.project_id).join(Category, Project.category == Category.id).join(KnowledgeArea, Project.knowledge_area == KnowledgeArea.id).add_columns(Category.name, KnowledgeArea.name).filter(Author.author_id == user_id).all()
    
    dumped_results = []
    
    if user_projects:
        for p in user_projects:
            project_dumped = project_schema.dump(p[0])
            project_dumped['category'] = p[1]
            project_dumped['knowledge_area'] = p[2]

            authors = User.query.join(Author, Author.author_id == User.id).filter(Author.project_id == project_dumped['id']).all()
            authors_list = users_schema.dump(authors)

            project_dumped['thesis_advisors'] = []

            for a in authors_list:
                if a['type_user'] == 0:
                    project_dumped['student'] = a['name']
                else:
                    project_dumped['thesis_advisors'].append(a['name'])
            
            dumped_results.append(project_dumped)
        
        return jsonify({'message': 'success', 'data': dumped_results}), 200
    else:
        return jsonify({'message': '_no_projects_', 'data': False}), 200
