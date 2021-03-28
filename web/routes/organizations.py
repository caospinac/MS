from services import organizations as service
from schemas.organization import CreateSchema
from ._utils import Router


router = Router(prefix='/organizations')


@router.get('/')
def get():
    return service.get_list()


@router.post('/')
def create(payload: CreateSchema):
    return service.create(payload)
