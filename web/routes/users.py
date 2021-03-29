from uuid import UUID

from services import users as service
from schemas.user import CreateSchema, UpdateSchema
from ._utils import Router


router = Router(prefix='/users')


@router.get('/')
def users(oid: UUID):
    return service.get_list(oid)


@router.post('/')
def create(oid: UUID, payload: CreateSchema):
    return service.create(oid, payload)


@router.put('/{ident}')
def update(ident: UUID, payload: UpdateSchema):
    return service.update(ident, payload)
