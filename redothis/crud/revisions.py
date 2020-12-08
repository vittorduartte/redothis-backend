from flask import jsonify, request
from ..extensions.database import database as db
from ..models import Revision, revision_schema, revisions_schema

def register_revision():
    submission_id = request.json['submission_id']
    create_by = request.json['user_id']
    comments = request.json['comments']
    attachment_filepath = request.json['attachment_filepath']

    if comments is None and attachment_filepath is None:
        return jsonify({'message': 'no comments or attachments on revision', 'data': False}), 500
    
    revision = Revision(submission_id, create_by, comments, attachment_filepath)
    
    try:
        db.session.add(revision)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data:': revision_schema.dump(revision)}), 201
    except:
        return jsonify({'message':'error on transaction', 'data':False}), 200


def get_submission_revisions():
    submission_id = request.json['submission_id']

    submission_revisions = Revision.query.filter_by(submission_id=submission_id)

    if submission_revisions.first():
        return jsonify({'message': 'success', 'data': revisions_schema.dump(submission_revisions)}), 200
    else:
        return jsonify({'message': '_no_revisions_', 'data': False}), 200
