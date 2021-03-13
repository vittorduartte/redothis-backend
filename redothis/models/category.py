from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

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