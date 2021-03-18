from services import UsersService
from ._utils import Router


service = UsersService()
router = Router(prefix='/users')


@router.get('/')
def users():
    return service.get_users()
