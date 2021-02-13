#!/bin/bash

docker-compose build
python3 -m venv web/.venv
web/.venv/bin/pip install --upgrade pip
web/.venv/bin/pip install -r web/requirements-dev.txt
web/.venv/bin/pip install -r web/requirements.txt

echo "All done."
echo "Run 'docker-compose up' to start services and finish building"
