from flask_marshmallow import Marshmallow

marsh = Marshmallow()

def init(app):
    marsh.init_app(app)