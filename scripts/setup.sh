#!/bin/bash

if [ ! -f .env ]; then
    cp .env.tmpl .env
fi

python3 -m pip install -U --upgrade pip
python3 -m pip install -U pipenv
PIPENV_VENV_IN_PROJECT=1 python3 -m pipenv install -d
.venv/bin/pip install --upgrade pip
.venv/bin/pip install pipenv
source .venv/bin/activate

echo "OK, let's hack!"
