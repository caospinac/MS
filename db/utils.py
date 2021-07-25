import sqlalchemy as sa

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from lib.const import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME


def get_engine() -> Engine:
    db_endpoint = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

    return sa.create_engine(db_endpoint, echo=True)


def get_session() -> Session:
    return Session(bind=get_engine())
