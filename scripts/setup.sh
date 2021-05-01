#!/bin/bash

microservices=(
    postgres
    redis
    web
    pgadmin
)

for ms in "${microservices[@]}"; do
    if [ ! -f $ms/.env.local ]; then
        cp $ms/.env $ms/.env.local
    fi
done

docker-compose build

cd web

poetry install

cd ..

echo "All done."
echo "Run 'docker-compose up' to start services"
