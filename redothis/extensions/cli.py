import click
from ..misc import populate_database as pop
from ..extensions.database import database as db


def init(app):

    @app.cli.command()
    def init_database():
        """
        Função responsável pela criação das tabelas do banco de dados
        e todas as suas relações definidas na camada de modelos.
        """
        db.create_all()
        click.echo("Initialized the database")

    @app.cli.command()
    def populate_database():
        """
        Função responsável pela inserção de dados de teste no banco de
        dados anteriormente criado. Esta função requer a init_database.
        """
        pass
