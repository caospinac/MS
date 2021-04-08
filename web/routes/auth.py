from uuid import UUID

from schemas.auth import LoginSchema
from services import auth
from ._utils import Router


router = Router()


@router.post('/login')
def login(oid: UUID, payload: LoginSchema):

    return auth.authenticate(oid, payload)
