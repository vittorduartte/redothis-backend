from flask_jwt import JWT
from ..controllers.auth import indentity
from ..controllers.auth import authenticate


def init(app):
    jwt = JWT(app, authenticate, indentity)
