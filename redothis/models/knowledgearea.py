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
