from flask import Flask
from .resources import users
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

    return app