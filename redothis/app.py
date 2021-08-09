from flask import Flask
from .resources import users
from .resources import courses
from .resources import degrees
from .resources import projects
from .resources import categories
from .resources import submissions
from .resources import revisions
from .resources import knowledge_areas
from .resources import auth
from .extensions import database
from .extensions import cors
from .extensions import cli
from .extensions import jwt
import os


def create_app():
    app = Flask(__name__)
#   Variáveis de configurações
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI")
    app.config["JWT_REQUIRED_CLAIMS"] = list(os.getenv("JWT_REQUIRED_CLAIMS"))

#   Iniciando as extensões
    database.init(app)
    cors.init(app)
    cli.init(app)
    jwt.init(app)

#   Iniciando as rotas
    users.init(app)
    courses.init(app)
    degrees.init(app)
    projects.init(app)
    categories.init(app)
    submissions.init(app)
    revisions.init(app)
    knowledge_areas.init(app)
    auth.init(app)

    return app
