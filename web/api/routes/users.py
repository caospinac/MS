from uuid import UUID

from fastapi import Depends

from services import users as service
from schemas.user import CreateSchema, UpdateSchema, UpdatePasswordSchema
from api.utils import Router
from api.deps import get_db


router = Router(prefix='/v1/users')


@router.get('/')
def users(oid: UUID, db=Depends(get_db)):
    return service.get_list(db, oid)


@router.post('/')
def create(oid: UUID, payload: CreateSchema, db=Depends(get_db)):
    return service.create(db, oid, payload)


@router.put('/{ident}')
def update(ident: UUID, payload: UpdateSchema, db=Depends(get_db)):
    return service.update(db, ident, payload)


@router.delete('/{ident}')
def delete(ident: UUID, db=Depends(get_db)):
    return service.delete(db, ident)


@router.patch('/{ident}/restore')
def restore(ident: UUID, db=Depends(get_db)):
    return service.restore(db, ident)


@router.put('/{ident}/password')
def update_password(ident: UUID, payload: UpdatePasswordSchema,
                    db=Depends(get_db)):
    return service.update_password(db, ident, payload)
