from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def init(app):
    database.init_app(app)