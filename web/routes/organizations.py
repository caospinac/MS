from services import OrganizationsService
from schemas.organization import CreateSchema
from ._utils import Router


service = OrganizationsService()
router = Router(prefix='/organizations')


@router.get('/')
def get():
    return service.get_organizations()


@router.post('/')
def create(payload: CreateSchema):
    return service.create(payload)
