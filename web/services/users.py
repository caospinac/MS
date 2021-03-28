from sqlalchemy.orm import Session

from models import Organization
from db import use_db


@use_db
def get_list(oid: str, db: Session=None):
    org = Organization.get(db, oid)
    return org.users
