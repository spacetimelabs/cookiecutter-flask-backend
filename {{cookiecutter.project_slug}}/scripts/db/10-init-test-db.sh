#!/bin/bash

set -e

# CREATE DATABASE LC_COLLATE 'pt_BR.UTF-8' LC_CTYPE 'pt_BR.UTF-8' pydaria_test;

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE {{cookiecutter.project_slug}}_test;
    GRANT ALL PRIVILEGES ON DATABASE {{cookiecutter.project_slug}}_test TO {{cookiecutter.project_slug}};
EOSQL
