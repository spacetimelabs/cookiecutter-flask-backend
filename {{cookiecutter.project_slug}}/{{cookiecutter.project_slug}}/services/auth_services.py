from {{cookiecutter.project_slug}}.models.auth import User


def list_users():
    return User.query.all()
