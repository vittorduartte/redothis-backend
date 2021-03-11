from flask import request, jsonify
from ..extensions.database import database as db
from ..models import (
    Category,
    Submission,
    submission_schema,
    submissions_schema,
    KnowledgeArea
)
from ..models.user import (
    User,
    user_schema,
    users_schema
)
from ..models.user import (
    Author,
    authors_schema
)
from ..models.course import (
    Course,
    course_schema
)
from ..models.degree import Degree
from ..models.project import (
    Project,
    project_schema,
    project_schemas
)
from .users import get_user_by_id


def register_project():
    title = request.json['title']
    subtitle = request.json['subtitle']
    category = request.json['category']
    knowledge_area = request.json['knowledge_area']
    students = request.json['students']
    tutors = request.json['tutors']
    create_by = request.json['create_by']

    project = Project(title, subtitle, category, knowledge_area, create_by)
    db.session.add(project)

    for s in students:
        student_in_process = Author.query.filter_by(author_id=s).first()
        if(student_in_process):
            return jsonify({'message': 'user already working', 'data': False}), 200

    try:
        db.session.add(Author(create_by, project.id))
        for s in students:
            db.session.add(Author(s, project.id))
        if(len(tutors) == 0):
            pass
        else:
            for t in tutors:
                db.session.add(Author(t, project.id))

        db.session.commit()
        return jsonify({'message': 'resource created', 'data': project_schema.dump(project)}), 201
    except Exception as e:
        return jsonify({'message': 'error on transaction', 'data': False}), 200


def get_users_from_project(project_id):
    authors = User.query.join(Author, Author.author_id == User.id).join(Degree, User.degree_id == Degree.id).join(
        Course, User.course_id == Course.id).add_columns(Degree.name, Course.name).filter(Author.project_id == project_id).all()

    result = []

    for auth in authors:
        a = user_schema.dump(auth[0])
        a['degree'] = auth[1]
        a['course'] = auth[2]
        a['type_user'] = a['type_user'] = "Estudante" if a['type_user'] == 0 else "Professor"

        result.append(a)

    return result


def get_users_by_project(project_id):
    users = get_users_from_project(project_id)

    if len(users) > 0:
        return jsonify({'message': 'success', 'data': users}), 200
    else:
        return jsonify({'message': '_invalid_project_id__', 'data': False}), 200


def get_project_by_id():
    project_id = request.args.get('id')

    result = Project.query.join(Category, Project.category == Category.id).join(KnowledgeArea, Project.knowledge_area ==
                                                                                KnowledgeArea.id).add_columns(Category.name, KnowledgeArea.name).filter(Project.id == project_id).first()

    if result:
        project = project_schema.dump(result[0])
        project['category'] = result[1]
        project['knowledge_area'] = result[2]

        authors = get_users_from_project(project['id'])

        project['students'] = []
        project['thesis_advisors'] = []
        project['course'] = None

        for a in authors:
            if a['type_user'] == 'Estudante':
                project['students'].append(a)
                if project['course'] is None:
                    project['course'] = course_schema.dump(
                        Course.query.filter_by(id=a['course_id']).first())['name']

            else:
                project['thesis_advisors'].append(a)

        return jsonify({'message': 'success', 'data': project}), 200
    else:
        return jsonify({'message': '_no_projects_', 'data': False}), 200


def get_projects_by_user(user_id):
    user_projects = Project.query.join(Author, Project.id == Author.project_id).join(Category, Project.category == Category.id).join(
        KnowledgeArea, Project.knowledge_area == KnowledgeArea.id).add_columns(Category.name, KnowledgeArea.name).filter(Author.author_id == user_id).all()

    dumped_results = []

    if user_projects:
        for p in user_projects:
            project_dumped = project_schema.dump(p[0])
            project_dumped['category'] = p[1]
            project_dumped['knowledge_area'] = p[2]

            authors = get_users_from_project(project_dumped['id'])

            project_dumped['students'] = []
            project_dumped['thesis_advisors'] = []
            project_dumped['course'] = None

            for a in authors:
                if a['type_user'] == 'Estudante':
                    project_dumped['students'].append(a)

                    if project_dumped['course'] is None:
                        project_dumped['course'] = course_schema.dump(
                            Course.query.filter_by(id=a['course_id']).first())['name']

                else:
                    project_dumped['thesis_advisors'].append(a)

            dumped_results.append(project_dumped)

        return jsonify({'message': 'success', 'data': dumped_results}), 200
    else:
        return jsonify({'message': '_no_projects_', 'data': False}), 200
