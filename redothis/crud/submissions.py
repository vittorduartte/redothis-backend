from flask import request, jsonify
from ..extensions.database import database as db
from ..models import (
    Submission,
    submission_schema,
    submissions_schema,
    Revision,
    revision_schema,
    revisions_schema,
    User,
    user_schema
)
from .revisions import get_user_from_revision


def register_submission():
    description = request.json['description']
    filepath = request.json['filepath']
    project_id = request.json['project_id']
    create_by = request.json['user_id']

    submission = Submission(description, filepath, project_id, create_by)

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

        submission['create_by'] = get_user_from_revision(
            submission['create_by'])

        revisions = Revision.query.filter(
            Revision.submission_id == submission['id']).all()

        revisions = revisions_schema.dump(revisions)

        for r in revisions:
            r['create_by'] = get_user_from_revision(r['create_by'])

        submission['revisions'] = revisions

        if len(submission['revisions']) > 0:
            submission['revised'] = 1
        else:
            submission['revised'] = 0

        return jsonify({'message': 'success',
                        'data': submission}), 200
    else:
        return jsonify({'message': '_no_valid_submission_id_', 'data': False}), 200


def get_project_submissions(project_id):
    project_submissions = Submission.query.filter_by(project_id=project_id)

    if project_submissions.first():
        project_submissions = submissions_schema.dump(project_submissions)

        for p in project_submissions:
            p['create_by'] = get_user_from_revision(
                p['create_by'])

            revisions = Revision.query.filter(
                Revision.submission_id == p['id']).all()

            revisions = revisions_schema.dump(revisions)

            for r in revisions:
                r['create_by'] = get_user_from_revision(r['create_by'])

            p['revisions'] = revisions

            if len(p['revisions']) > 0:
                p['revised'] = 1
            else:
                p['revised'] = 0

        return jsonify({'message': 'success',
                        'data': project_submissions}), 200
    else:
        return jsonify({'message': '_no_submissions_', 'data': False}), 200
