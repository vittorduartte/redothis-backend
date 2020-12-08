from flask import Flask
from .resources import users, courses, degrees, projects, categories, submissions, revisions, knowledge_areas
from .extensions import database, cors

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='1234567890'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

#   Iniciando as extensões
    database.init(app)
    cors.init(app)
    
#   Iniciando as rotas
    users.init(app)
    courses.init(app)
    degrees.init(app)
    projects.init(app)
    categories.init(app)
    submissions.init(app)
    revisions.init(app)
    knowledge_areas.init(app)

    return app
