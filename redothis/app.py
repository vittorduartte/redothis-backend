from flask import Flask
from .resources import users
from .extensions import database

def create_app():
    app = Flask(__name__)

#   Iniciando as extensões
    database.init(app)
    
#   Iniciando as rotas
    users.init(app)

    return app