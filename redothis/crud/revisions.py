from flask import jsonify, request
from ..extensions.database import database as db
from ..models import (
    Revision,
    revision_schema,
    revisions_schema,
    User,
    user_schema
)

from ..models.course import Course
from ..models.degree import Degree

def register_revision():
    submission_id = request.json['submission_id']
    create_by = request.json['user_id']
    comments = request.json['comments']
    attachment_filepath = request.json['attachment_filepath']

    if comments is None and attachment_filepath is None:
        return jsonify({'message': 'no comments or attachments on revision', 'data': False}), 500

    revision = Revision(submission_id, create_by,
                        comments, attachment_filepath)

    try:
        db.session.add(revision)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data:': revision_schema.dump(revision)}), 201
    except:
        return jsonify({'message': 'error on transaction', 'data': False}), 200


def get_user_from_revision(user_id):
    user = User.query.join(Degree, User.degree_id == Degree.id).join(
        Course, User.course_id == Course.id).add_columns(Degree.name, Course.name).filter(User.id == user_id).first()

    if user:
        u = user_schema.dump(user[0])
        u['degree'] = user[1]
        u['course'] = user[2]
        u['type_user'] = "Estudante" if u['type_user'] == 0 else "Professor"

        return u

    return None


def get_revision_by_id():
    revision_id = request.args.get('id')

    revision = Revision.query.filter(Revision.id == revision_id).first()

    if revision:
        result = revision_schema.dump(revision)
        result['create_by'] = get_user_from_revision(result['create_by'])

        return jsonify({'message': 'sucess', 'data': result}), 200
    else:
        return jsonify({'message': '_invalid_revision_id_', 'data': False}), 200


def get_submission_revisions(submission_id):
    submission_revisions = Revision.query.filter_by(
        submission_id=submission_id).all()

    if len(submission_revisions) > 0:
        revisions = revisions_schema.dump(submission_revisions)

        for r in revisions:
            r['create_by'] = get_user_from_revision(r['create_by'])

        return jsonify({'message': 'success', 'data': revisions}), 200
    else:
        return jsonify({'message': '_no_revisions_', 'data': False}), 200
