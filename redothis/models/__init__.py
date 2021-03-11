import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class KnowledgeArea(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name


class KnowledgeAreaSchema(marsh.SQLAlchemyAutoSchema):
    class Meta():
        model = KnowledgeArea


knowledgeArea_schema = KnowledgeAreaSchema()
knowledgeAreas_schema = KnowledgeAreaSchema(many=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name


class CategorySchema(marsh.SQLAlchemyAutoSchema):
    class Meta():
        model = Category


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


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
