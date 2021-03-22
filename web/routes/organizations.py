from services import OrganizationsService
from schemas.organization import CreateSchema
from ._utils import Router


service = OrganizationsService()
router = Router(prefix='/organizations')


@router.get('/')
def get():
    return service.get_all()


@router.post('/')
def create(payload: CreateSchema):
    return service.create(payload)


@router.get('/{ident}')
def get_one(ident: str):
    return service.get_by_id(ident)
