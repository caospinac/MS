from typing import Generator

from fastapi import Security, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

import models
from services import users
from lib import Jwt, Redis
from db.utils import get_session


def get_db() -> Generator:
    try:
        db = get_session()
        yield db

    finally:
        db.close()


def authenticated(
    credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())
) -> str:
    try:
        if credentials:
            token_data = Jwt.verify_token(credentials.credentials)

            session_key = Redis.build_key('session',
                                          token_data.uid, token_data.sid)
            session_user = Redis.load(session_key)

            return session_user['id']

        return None

    except Exception as e:
        raise HTTPException(403, detail='Invalid authentication code.') from e


def get_current_user(
    user_id: str = Depends(authenticated), db: Session = Depends(get_db)
) -> models.User:
    user = users.get(db, user_id)

    return user
