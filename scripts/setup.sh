#!/bin/bash

microservices=(
    postgres
    redis
    server
    pgadmin
)

for ms in "${microservices[@]}"; do
    if [ ! -f $ms/.env ]; then
        cp $ms/.env.tmpl $ms/.env
    fi
done

docker-compose build

(
    cd server
    PIPENV_VENV_IN_PROJECT=1 pipenv install
)

echo "All done."
echo "Run 'docker-compose up' to start services"
