
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_debugtoolbar import DebugToolbarExtension

from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.auth import User

admin = Admin()


def init_app(app):
    admin.init_app(app)
    admin.add_view(UserView(
        User, db.session,
        category='Users',
    ))
    DebugToolbarExtension(app)


class UserView(sqla.ModelView):
    column_list = 'id username first_name last_name email is_active created_at'.split()
    column_filters = 'username is_active'.split()
    can_delete = True
    can_export = True
