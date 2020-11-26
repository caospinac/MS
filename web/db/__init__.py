from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


from lib.const import DB_HOST

engine = create_engine(DB_HOST, echo=True)
Base = declarative_base()
