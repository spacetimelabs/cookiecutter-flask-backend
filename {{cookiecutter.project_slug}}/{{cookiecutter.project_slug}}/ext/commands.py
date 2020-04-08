import click
from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.auth import User


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        User(username="admin"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return User.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option("--username", "-n")
    def add_user(username):
        """Adds a new user to the database"""
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return user
