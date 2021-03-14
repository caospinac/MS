import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()

class Model(Base):

    __abstract__ = True

    id = sa.Column(UUID, primary_key=True,
                   default=uuid.uuid4, unique=True, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(
        sa.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime, default=None)

    @staticmethod
    def default_value(column):
        return lambda cxt: cxt.get_current_parameters()[column]

