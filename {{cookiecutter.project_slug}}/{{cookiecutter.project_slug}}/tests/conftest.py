import os
import pytest
import sqlalchemy as sa
import factory
from datetime import datetime, timezone
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.auth import User


@pytest.fixture(scope="session")
def app():
    os.environ["FLASK_ENV"] = "testing"
    app = create_app()
    with app.app_context():
        db.create_all(app=app)
        # flask_migrate.upgrade(revision="heads")
        yield app
        db.drop_all(app=app)


@pytest.fixture(scope="function")
def db_session(app):
    conn = db.engine.connect()
    trans = conn.begin()

    session = Session(bind=conn)
    session.begin_nested()

    # then each time that SAVEPOINT ends, reopen it
    @sa.event.listens_for(db.session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.expire_all()
            session.begin_nested()

    db.session.begin_nested()

    UserFactory._meta.sqlalchemy_session = db.session

    yield db.session

    # rollback everything
    trans.rollback()
    conn.close()
    db.session.remove()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = User

    id = factory.Sequence(int)
    username = factory.Faker('first_name')
    password = 'abc'
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_active = True
    created_at = datetime.now(timezone.utc)
