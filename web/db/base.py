import sqlalchemy as sa


from lib.const import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

db_endpoint = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = sa.create_engine(db_endpoint, echo=True)
