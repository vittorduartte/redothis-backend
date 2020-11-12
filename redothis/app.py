from flask import Flask
from .ext import database as db
from .ext import marshmallow as ma
from .routes import users


def create_app():
    app = Flask(__name__)

#   Iniciando as extensões
    db.init(app)
    ma.init(app)

#   Iniciando as rotas
    users.init(app)

    return app