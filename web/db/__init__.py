import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


from lib.const import DB_HOST

engine = sa.create_engine(DB_HOST, echo=True)

metadata = sa.MetaData(
    naming_convention={
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s'
    }
)

Base = declarative_base(metadata=metadata)
