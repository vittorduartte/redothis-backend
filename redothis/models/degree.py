import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

class DegreeSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Degree

degree_schema = DegreeSchema()
degrees_schema = DegreeSchema(many=True)