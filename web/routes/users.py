from services import users as service
from ._utils import Router


router = Router(prefix='/users')


@router.get('/')
def users():
    return service.get_list()
