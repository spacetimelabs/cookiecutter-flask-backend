import mock
from {{cookiecutter.project_slug}}.models.auth import User


@mock.patch('{{cookiecutter.project_slug}}.services.auth_services.list_users')
def test_should_list_users(list_users_mock, client):

    # Dado um serviço mock
    list_users_mock.return_value = [
        User(id=1, username='John'),
        User(id=2, username='Trish'),
    ]

    # Quando chamamos a api de usuários
    response = client.get(
        '/api/v1/auth/users/',
        headers={'content-type': 'application/json'},
    )

    # Então
    assert response.status_code == 200
    assert response.json == {
        'users': [
            {
                'id': 1,
                'username': 'John',
                'email': None,
                'first_name': None,
                'is_active': None,
                'last_name': None,
                'password': None,
                'created_at': None,
            },
            {
                'id': 2,
                'username': 'Trish',
                'email': None,
                'first_name': None,
                'is_active': None,
                'last_name': None,
                'password': None,
                'created_at': None,
            }
        ]
    }
