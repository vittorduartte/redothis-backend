import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type_user = db.Column(db.Integer, nullable=False)
    university = db.Column(db.String(200), nullable=False)
    degree = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(200), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, email, password, name, type_user, university, degree, course):
        self.email = user_email
        self.password = password
        self.name = name
        self.type_user = type_user
        self.university = university
        self.degree = degree
        self.course = course

class UsersSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name', 'type_user', 'university', 'degree', 'course', 'create_on')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
