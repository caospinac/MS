import models

from fastapi import Security, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from schemas.jwt import TokenData
from lib import Jwt
from db.utils import get_session
from services import users


def get_db():
    try:
        db = get_session()
        yield db

    finally:
        db.close()


def authenticated(
    credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())
) -> TokenData:
    try:
        if credentials:
            return Jwt.verify_token(credentials.credentials)

    except:
        pass

    raise HTTPException(403, detail='Invalid authentication code.')


def get_current_user(
  token_data: TokenData = Depends(authenticated), db: Session = Depends(get_db)
) -> models.User:
    user = users.get(db, token_data.uid)

    return user
