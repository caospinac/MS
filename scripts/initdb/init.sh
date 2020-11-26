#!/bin/bash

psql -U "${PGUSER:-postgres}" \
    -p ${PGPORT:-5432} \
    -c "CREATE DATABASE $PGDATABASE"
