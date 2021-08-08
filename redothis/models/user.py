import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type_user = db.Column(db.Integer, nullable=False)
    degree_id = db.Column(db.Integer, db.ForeignKey(
        'degree.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.id'), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, email, password, name, type_user, degree_id, course_id):
        self.email = email
        self.password = password
        self.name = name
        self.type_user = type_user
        self.degree_id = degree_id
        self.course_id = course_id


class UserSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name', 'type_user',
                  'degree_id', 'course_id', 'create_on')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
