#!/bin/bash

PARAMS=''
for i in "$@"; do 
    i="${i//\\/\\\\}"
    PARAMS="$PARAMS \"${i//\"/\\\"}\""
done

bash -c "web/.venv/bin/python -m alembic $PARAMS"