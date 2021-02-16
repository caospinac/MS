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

ALEMBIC_DIR="web/db"

if [ ! -d $ALEMBIC_DIR ]; then
    web/.venv/bin/python -m alembic init $ALEMBIC_DIR
    sed -i '1 i\# pylint: disable=no-member' "$ALEMBIC_DIR/env.py"
fi

eval $(egrep -v '^#' .env | xargs)

DB_ENDPOINT=$POSTGRES_SERVER
if [ $POSTGRES_PORT ]; then
    DB_ENDPOINT="$DB_ENDPOINT:$POSTGRES_PORT"
fi

NEW_LINE="sqlalchemy.url = postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD"
NEW_LINE="$NEW_LINE@$DB_ENDPOINT/$POSTGRES_DB"

sed -i "/sqlalchemy.url/c$NEW_LINE" alembic.ini

echo "All done."
echo "Run 'docker-compose up' to start services"
