import functools

import sqlalchemy as sa
from sqlalchemy.orm import Session

from lib.const import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


def get_engine():
    db_endpoint = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    return sa.create_engine(db_endpoint, echo=True)


def get_session():
    return Session(bind=get_engine())


def use_db(wrapped):

    @functools.wraps(wrapped)
    def wrapper(*args, **kwargs):
        db = get_session()
        result = wrapped(*args, **kwargs, db=db)
        return result

    return wrapper
