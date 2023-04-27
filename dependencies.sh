#!/bin/bash

set -eux

python -m pip install --upgrade pip
wget https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py
export POETRY_HOME=/opt/poetry
python install-poetry.py --version 1.2.0
$POETRY_HOME/bin/poetry --version
$POETRY_HOME/bin/poetry install
