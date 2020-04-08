
# Cookiecutter Flask Backend

Flask starter project for [Cookiecutter](https://github.com/audreyr/cookiecutter).

This project is used to generate a great architecture Flask project. It's designed for a web application that uses server-side API and its backoffice (Admin).
This structure is based on this amazing repository: [codeshow / arquitetura-flask](https://github.com/codeshow/003-arquitetura-flask)

Flask Extensions:

- Backoffice using [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/)
- Allowing CORS requests with [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)
- ORM and database migrations using
  - [SQLAlchemy](https://www.sqlalchemy.org/)
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

Devops & QA:

-  [DotEnv](https://pypi.org/project/python-dotenv/)
-  [IPython Shell](https://pypi.org/project/flask-shell-ipython/)
- Linter using [Flake8](https://flake8.pycqa.org/en/latest/)
- Postgres container for development. Using [Docker](https://hub.docker.com/_/postgres)

Testing:
- Tests using [Pytest](https://docs.pytest.org/en/latest/)
- Mocking the database using [Factory-boy](https://factoryboy.readthedocs.io/en/latest/)


## Quick Start

First, get Cookiecutter installed:

```sh

pip install cookiecutter

```

Now run it against this repo:

```sh

cookiecutter https://github.com/spacetimelabs/cookiecutter-flask-backend.git
```

You'll be prompted for some values. Provide them using your own information and a Flask project will be created for you.

```sh
project_name [My Awesome Project]: My Blog
project_slug [my_blog]:
author_name [Roger Camargo]:
domain_name [example.com]: myblog.com
Select postgresql_version:
1 - 11
2 - 10
Choose from 1, 2 [1]: 1
```

Enter the project and take a look around:
```sh
cd my_blog
ls -lha

```

Start the Postgres database (production like)

```sh
docker-compose up --build -d

```

Install the libpq-dev library if you don't have it. In Linux Mint, the command to install the library will look like this:

```sh
apt-get install libpq-dev        

```

Install the project's dependencies. It's better use a [Virtualenv](https://virtualenv.pypa.io/en/latest/)

```sh
virtualenv ~/.ve/myblog
source ~/.ve/myblog/bin/activate
pip install -r requirements-devs.txt

```

Create the database tables. Thanks [Alembic](https://alembic.sqlalchemy.org/)

```sh
# Just the first time
flask db upgrade
```

Start your project
```sh
flask run
```

Check your project running

```sh
# Create a new user using the Admin
http://localhost:5000/admin

# Get the users using the api
http://localhost:5000/api/v1/auth/users

```

## Testing
Create another database for tests

```sh
# Just the first time
./scripts/db/prepare_test_db.sh
```

Run the tests

```sh
pytest

```

## Community

If you think you found a bug or want to request a feature, please open an issue.
