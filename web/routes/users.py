from services import UsersService
from ._utils import Router


service = UsersService()
router = Router(prefix='/users')


@router.get('/')
def users():
    s = service.get_users()
    return s
