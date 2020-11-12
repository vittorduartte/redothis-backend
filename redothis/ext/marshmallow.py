from flask_marshmallow import Marshmallow 

ma = Marshmallow()


def init(app):
    ma.init_app(app)