#!/bin/bash

if command -v pipenv >/dev/null 2>&1; then
    pipenv install --dev
fi
