import datetime
from ..extensions.database import database as db
from ..extensions.marshmallow import marsh

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    courses = db.relationship('Course', backref="university", lazy=True)

    def __init__(self, name):
        self.name = name

class UniversitySchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'courses')

university_schema = UniversitySchema()
universitys_schema = UniversitySchema(many=True)

class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

class DegreeSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name')

degree_schema = DegreeSchema()
degrees_schema = DegreeSchema(many=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    users = db.relationship('User', backref='course', lazy=True)

    def __init__(self, name, university_id):
         self.name = name
         self.university_id = university_id

class CourseSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'name', 'university_id', 'users')

course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type_user = db.Column(db.Integer, nullable=False)
    degree_id = db.Column(db.Integer, db.ForeignKey('degree.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, email, password, name, type_user, university, degree, course):
        self.email = email
        self.password = password
        self.name = name
        self.type_user = type_user
        self.university = university
        self.degree = degree
        self.course = course

class UserSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'email', 'password', 'name', 'type_user', 'university', 'degree', 'course')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(200), nullable=True)
    knowledge_area = db.Column(db.String(200), nullable=True)
    create_on = db.Column(db.DateTime, default=datetime.datetime.now())
    authors = db.relationship('Author', backref="project", lazy=True)

    def __init__(self, title, subtitle, category, knowledge_area):
        self.title = title
        self.subtitle = subtitle
        self.category = category
        self.knowledge_area = knowledge_area
    
class ProjectSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'title', 'subtitle', 'cotegory', 'knowledge_area')

project_schema = ProjectSchema()
project_schemas = ProjectSchema(many=True)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer,db.ForeignKey('project.id'), nullable=False)

    def __init__(self, author_id, project_id):
        self.author_id = author_id
        self.project_id = project_id