from typing import List, Union

from fastapi import Depends
from sqlalchemy.orm.session import Session

from models.organization import Organization
from services import organizations as service
from schemas.organization import CreateSchema, CompleteCreationSchema
from api.utils import Router
from api.deps import get_db


router = Router(prefix='/v1/organizations')


@router.get('/')
def get_list(db: Session = Depends(get_db)) -> List[Organization]:
    return service.get_list(db)


@router.get('/{ident}')
def get(
    ident: str, db: Session = Depends(get_db)
) -> Union[Organization, None]:
    return service.get(db, ident)


@router.post('/')
def create(
    payload: CreateSchema, db: Session = Depends(get_db)
) -> Organization:
    return service.create(db, payload)


@router.post('/{ident}/verify')
def complete_creation(
    ident: str, payload: CompleteCreationSchema, db: Session = Depends(get_db)
) -> Organization:
    return service.complete_creation(db, ident, payload)
