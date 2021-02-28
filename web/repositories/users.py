from sqlalchemy.orm import Session
from models import User

session = Session()
query = session.query(User)
