from flask import request, jsonify
from ..extensions.database import database as db
from ..models import Submission, submission_schema, submissions_schema

def register_submission():
    description = request.json['description']
    filepath = request.json['filepath']
    project_id = request.json['project_id']

    submission = Submission(description, filepath, project_id)

    try:
        db.session.add(submission)
        db.session.commit()
        return jsonify({'message': 'resource created',
                        'data:': submission_schema.dump(submission)}), 201
    except:
        return jsonify({'message':'error on transaction', 'data':False}), 200



def get_project_submissions():
    project_id = request.json['project_id']

    project_submissions = Submission.query.filter_by(project_id=project_id)

    if project_submissions.first():
        return jsonify({'message': 'success', 'data': submissions_schema.dump(project_submissions)}), 200
    else:
        return jsonify({'message': '_no_submissions_', 'data': False}), 200
