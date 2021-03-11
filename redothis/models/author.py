from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)

    def __init__(self, author_id, project_id):
        self.author_id = author_id
        self.project_id = project_id


class AuthorSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'author_id', 'project_id')


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)