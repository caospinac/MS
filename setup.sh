#!/bin/bash

if [ ! -f .env ]; then
    cp .env.template .env
fi

docker-compose build

if [ ! -d web/.venv ]; then
    python3 -m venv web/.venv
    web/.venv/bin/pip install --upgrade pip
fi

web/.venv/bin/pip install -r web/requirements-dev.txt
web/.venv/bin/pip install -r web/requirements.txt

ALEMBIC_DIR="web/alem"

if [ ! -d $ALEMBIC_DIR ]; then
    web/.venv/bin/python -m alembic init $ALEMBIC_DIR
    eval $(egrep -v '^#' .env | xargs)

    NEW_LINE="sqlalchemy.url = postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD"
    NEW_LINE="$NEW_LINE@$POSTGRES_SERVER/$POSTGRES_DB"

    sed -i "/sqlalchemy.url/c$NEW_LINE" alembic.ini
    sed -i '1 i\# pylint: disable=no-member' "$ALEMBIC_DIR/env.py"
fi

echo "All done."
echo "Run 'docker-compose up' to start services"
