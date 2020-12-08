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


class UserSchema(marsh.SQLAlchemySchema):
    class Meta:
        model = User

    id = marsh.auto_field()
    email = marsh.auto_field()
    name = marsh.auto_field()
    type_user = marsh.auto_field()
    degree_id = marsh.auto_field()
    course_id = marsh.auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)


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

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)

    def __init__(self, author_id, project_id):
        self.author_id = author_id
        self.project_id = project_id

        
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=True)
    subtitle = db.Column(db.String(500), nullable=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    knowledge_area = db.Column(db.Integer, db.ForeignKey('knowledge_area.id'), nullable=True)
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
       fields = ('id', 'title', 'subtitle', 'category', 'knowledge_area', 'create_by', 'create_on')
    

project_schema = ProjectSchema()
project_schemas = ProjectSchema(many=True)


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


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(500), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'project.id'), nullable=False)

    def __init__(self, description, filepath, project_id):
        self.description = description
        self.filepath = filepath
        self.project_id = project_id

class SubmissionSchema(marsh.SQLAlchemyAutoSchema):
    class Meta():
        model = Submission

submission_schema = SubmissionSchema()
submissions_schema = SubmissionSchema(many=True)

class Revision(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    create_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.Column(db.String(1500), nullable=False)
    attachment_filepath = db.Column(db.String(1500), nullable=True)

    def __init__(self, submission_id, create_by, comments, attachment_filepath):
        self.submission_id = submission_id
        self.create_by = create_by
        self.comments = comments
        self.attachment_filepath = attachment_filepath

class RevisionSchema(marsh.SQLAlchemyAutoSchema):
    class Meta():
        model = Revision

revision_schema = RevisionSchema()
revisions_schema = RevisionSchema(many=True)
    
