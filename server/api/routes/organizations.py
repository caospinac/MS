from uuid import UUID

from fastapi import Depends

from services import organizations as service
from schemas.organization import CreateSchema, CompleteCreationSchema
from api.utils import Router
from api.deps import get_db


router = Router(prefix='/v1/organizations')


@router.get('/')
def get_list(db=Depends(get_db)):
    return service.get_list(db)


@router.get('/{ident}')
def get(ident: UUID, db=Depends(get_db)):
    return service.get(db, ident)


@router.post('/')
def create(payload: CreateSchema, db=Depends(get_db)):
    return service.create(db, payload)


@router.post('/{ident}/verify')
def complete_creation(ident: UUID, payload: CompleteCreationSchema,
                      db=Depends(get_db)):
    return service.complete_creation(db, ident, payload)
