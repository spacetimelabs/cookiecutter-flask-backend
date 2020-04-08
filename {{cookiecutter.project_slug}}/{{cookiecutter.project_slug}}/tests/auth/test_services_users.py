from {{cookiecutter.project_slug}}.services import auth_services
from {{cookiecutter.project_slug}}.tests.conftest import UserFactory


def test_should_return_an_empty_list(db_session):

    users = auth_services.list_users()

    assert users == []


def test_should_return_a_bunch_of_items(db_session):

    UserFactory.create_batch(10)

    users = auth_services.list_users()

    assert len(users) == 10
