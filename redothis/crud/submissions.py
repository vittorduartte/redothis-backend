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
        db.commit()
        return jsonify({'message': 'resource created',
                        'data:': submission_schema.dump(submission)}), 201
    except:
        return jsonify({'message':'error on transaction', 'data':False}), 200
