from uuid import UUID

from fastapi import Depends

from schemas.auth import LoginSchema
from services import auth
from api.utils import Router
from api.deps import get_current_user, get_db


router = Router()


@router.post('/login')
def login(oid: UUID, payload: LoginSchema, db=Depends(get_db)):

    return auth.authenticate(db, oid, payload)


@router.get('/me')
def me(current_user=Depends(get_current_user)):
    return current_user
