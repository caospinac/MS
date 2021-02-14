#!/bin/bash

docker-compose exec web sh -c "cd .. && alembic $*"
