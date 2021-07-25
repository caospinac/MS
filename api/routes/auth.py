from typing import Any

from fastapi import Depends
from sqlalchemy.orm.session import Session

import models
from schemas.auth import LoginSchema
from services import auth
from api.utils import Router
from api.deps import get_current_user, get_db


router = Router()


@router.post('/login')
def login(oid: str, payload: LoginSchema, db: Session = Depends(get_db)) -> Any:

    return auth.authenticate(db, oid, payload)


@router.get('/me')
def me(current_user: models.User = Depends(get_current_user)) -> models.User:
    return current_user
