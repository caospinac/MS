#!/bin/bash

psql -U "${POSTGRES_USER:-postgres}" \
    -p ${DB_PORT:-5432} \
    -c "CREATE DATABASE $DB_NAME"
