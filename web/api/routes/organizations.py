from uuid import UUID

from services import organizations as service
from schemas.organization import CreateSchema, CompleteCreationSchema
from api.utils import Router


router = Router(prefix='/v1/organizations')


@router.get('/')
def get_list():
    return service.get_list()


@router.get('/{ident}')
def get(ident: UUID):
    return service.get(ident)


@router.post('/')
def create(payload: CreateSchema):
    return service.create(payload)


@router.post('/{ident}/verify')
def complete_creation(ident: UUID, payload: CompleteCreationSchema):
    return service.complete_creation(ident, payload)
