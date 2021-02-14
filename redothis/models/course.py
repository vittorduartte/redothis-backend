import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        self.name = name

class CourseSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)