from sqlalchemy.orm import Session

from models import User
from db import use_db


@use_db
def get_list(db: Session=None):

    return User.get_list(db)
