from flask import request, jsonify
from ..extensions.database import database as db
from ..models import (
    Submission,
    submission_schema,
    submissions_schema,
    Revision,
    revision_schema,
    revisions_schema
)
from .revisions import get_user_from_revision


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
        return jsonify({'message': 'error on transaction', 'data': False}), 200


def get_submission_by_id():
    submission_id = request.args.get('id')

    submission = Submission.query.filter(
        Submission.id == submission_id).first()

    if submission:
        submission = submission_schema.dump(submission)

        revisions = Revision.query.filter(
            Revision.submission_id == submission['id']).all()

        revisions = revisions_schema.dump(revisions)

        for r in revisions:
            r['create_by'] = get_user_from_revision(r['create_by'])

        submission['revisions'] = revisions

        return jsonify({'message': 'success',
                        'data': submission}), 200


def get_project_submissions(project_id):
    project_submissions = Submission.query.filter_by(project_id=project_id)

    if project_submissions.first():
        project_submissions = submissions_schema.dump(project_submissions)

        for p in project_submissions:
            revisions = Revision.query.filter(
                Revision.submission_id == p['id']).all()

            revisions = revisions_schema.dump(revisions)

            for r in revisions:
                r['create_by'] = get_user_from_revision(r['create_by'])

            p['revisions'] = revisions

        return jsonify({'message': 'success',
                        'data': project_submissions}), 200
    else:
        return jsonify({'message': '_no_submissions_', 'data': False}), 200
