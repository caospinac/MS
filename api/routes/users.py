from typing import List

from fastapi import Depends
from sqlalchemy.orm.session import Session

from models.user import User
from services import users as service
from schemas.user import CreateSchema, UpdateSchema, UpdatePasswordSchema
from api.utils import Router
from api.deps import get_db


router = Router(prefix='/v1/users')


@router.get('/')
def users(oid: str, db: Session = Depends(get_db)) -> List[User]:
    return service.get_list(db, oid)


@router.post('/')
def create(
    oid: str, payload: CreateSchema, db: Session = Depends(get_db)
) -> User:
    return service.create(db, oid, payload)


@router.put('/{ident}')
def update(
    ident: str, payload: UpdateSchema, db: Session = Depends(get_db)
) -> User:
    return service.update(db, ident, payload)


@router.delete('/{ident}')
def delete(ident: str, db: Session = Depends(get_db)) -> None:
    return service.delete(db, ident)


@router.patch('/{ident}/restore')
def restore(ident: str, db: Session = Depends(get_db)) -> User:
    return service.restore(db, ident)


@router.put('/{ident}/password')
def update_password(
    ident: str, payload: UpdatePasswordSchema, db: Session = Depends(get_db)
) -> None:
    return service.update_password(db, ident, payload)
