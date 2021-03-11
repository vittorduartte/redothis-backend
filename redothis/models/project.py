import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)
    category = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=True)
    knowledge_area = db.Column(db.Integer, db.ForeignKey(
        'knowledge_area.id'), nullable=True)
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())
    authors = db.relationship('Author', backref="project", lazy=True)

    def __init__(self, title, subtitle, category, knowledge_area, create_by):
        self.title = title
        self.subtitle = subtitle
        self.category = category
        self.knowledge_area = knowledge_area
        self.create_by = create_by


class ProjectSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'title', 'subtitle', 'category',
                  'knowledge_area', 'create_by', 'create_on')


project_schema = ProjectSchema()
project_schemas = ProjectSchema(many=True)
