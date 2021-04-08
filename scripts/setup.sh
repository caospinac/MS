#!/bin/bash

if [ ! -f .env ]; then
    cp .env.template .env
fi

poetry install
docker-compose build

ALEMBIC_DIR="web/db"

if [ ! -d $ALEMBIC_DIR ]; then
    .venv/bin/python -m alembic init $ALEMBIC_DIR
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
