import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


from lib.const import DB_HOST

engine = sa.create_engine(DB_HOST, echo=True)

Base = declarative_base()
