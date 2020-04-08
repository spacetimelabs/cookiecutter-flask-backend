import os
from importlib import import_module

EXTENSIONS = [
    "{{cookiecutter.project_slug}}.ext.database",
    "{{cookiecutter.project_slug}}.ext.commands",
    "{{cookiecutter.project_slug}}.ext.admin",
    "{{cookiecutter.project_slug}}.ext.api",
    "{{cookiecutter.project_slug}}.blueprints.api.auth",
]


class ProductionConfig(object):
    DEBUG = False
    TESTING = False
    TITLE = "{{cookiecutter.project_slug}}"
    SECRET_KEY = os.getenv('SECRET_KEY', b'\xa0\xb9\xbc\xd4P\x7f\xb8G\x99\xda\x80\x8e\xe8\x12G\xf1')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ext.admin
    FLASK_ADMIN_SWATCH = 'flatly'
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(ProductionConfig):
    TITLE = "{{cookiecutter.project_slug}} DEV"
    DEBUG = True


class TestingConfig(ProductionConfig):
    TITLE = "{{cookiecutter.project_slug}} TEST"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://{{cookiecutter.project_slug}}:{{cookiecutter.project_slug}}2020@localhost/{{cookiecutter.project_slug}}_test')


def get_config_from_env():
    envname = os.getenv("FLASK_ENV", "development").lower()

    if envname == "production":
        return ProductionConfig()
    elif envname == "testing":
        return TestingConfig()
    return DevelopmentConfig()


def load_extensions(app):
    for extension in EXTENSIONS:
        mod = import_module(extension)
        mod.init_app(app)


def init_app(app):
    config = get_config_from_env()
    app.config.from_object(config)
