import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class Revision(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submission_id = db.Column(db.Integer, db.ForeignKey(
        'submission.id'), nullable=False)
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.Column(db.String(1500), nullable=False)
    attachment_filepath = db.Column(db.String(1500), nullable=True)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, submission_id, create_by, comments, attachment_filepath):
        self.submission_id = submission_id
        self.create_by = create_by
        self.comments = comments
        self.attachment_filepath = attachment_filepath


class RevisionSchema(marsh.Schema):
    class Meta():
        fields = ('id', 'submission_id', 'create_by',
                  'comments', 'attachment_filepath', 'create_on')


revision_schema = RevisionSchema()
revisions_schema = RevisionSchema(many=True)    