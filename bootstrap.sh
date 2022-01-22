#!/bin/sh
export FLASK_APP=./cashman/index.py
source $(~/.local/bin/pipenv --venv)/bin/activate
flask run -h 0.0.0.0
