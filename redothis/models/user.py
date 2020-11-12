import datetime
from ..ext.database import db
from ..ext.marshmallow import ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type_user = db.Column(db.Integer, nullable=False)
    university = db.Column(db.String(200), nullable=False)
    degree = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(200), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_email, password, name, 
                 type_user, university, degree, course):
        self.user_email = user_email
        self.password = password
        self.name = name
        self.type_user = type_user
        self.university = university
        self.degree = degree
        self.course = course


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_email', 'password', 'name', 'type_user', 
                  'university', 'degree', 'course', 'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)