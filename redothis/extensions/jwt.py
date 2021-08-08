from flask_jwt import JWT
from ..controllers.users import indentity
from ..controllers.users import authenticate


def init(app):
    jwt = JWT(app, authenticate, indentity)
