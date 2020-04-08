#!/bin/bash

docker exec {{cookiecutter.project_slug}}_db ./scripts/db/10-init-test-db.sh
