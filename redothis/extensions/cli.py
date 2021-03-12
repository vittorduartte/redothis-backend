import click
from ..misc import populate_database as pop
from ..extensions.database import database as db

def init(app):

    @app.cli.command()
    def initdb():
        """Populate your test database to development enviroment."""
        db.create_all()
        pop.init()
        click.echo("Initialized the database")
