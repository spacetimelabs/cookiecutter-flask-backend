from flask import Blueprint, jsonify
from {{cookiecutter.project_slug}}.services import auth_services

bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


def init_app(app):
    app.register_blueprint(bp)


@bp.route('/users/')
def list_users():
    users = auth_services.list_users()
    users = {
        'users': [user.to_dict() for user in users]
    }
    return jsonify(users)
