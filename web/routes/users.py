from uuid import UUID

from services import users as service
from ._utils import Router


router = Router(prefix='/users')


@router.get('/')
def users(oid: UUID):
    return service.get_list(oid)
