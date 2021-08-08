import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(500), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, description, filepath, project_id, create_by):
        self.description = description
        self.filepath = filepath
        self.project_id = project_id
        self.create_by = create_by


class SubmissionSchema(marsh.Schema):
    class Meta():
        fields = ('id', 'description', 'filepath',
                  'project_id', 'create_by', 'create_on')


submission_schema = SubmissionSchema()
submissions_schema = SubmissionSchema(many=True)
