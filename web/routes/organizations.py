from services import OrganizationsService
from schemas.organization import CreateSchema
from ._utils import Router


service = OrganizationsService()
router = Router(prefix='/organizations')


@router.get('/')
def get():
    s = service.get_organizations()
    return s


@router.post('/')
def create(payload: CreateSchema):
    result = service.create(payload)
    return result
