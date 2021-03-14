from fastapi import APIRouter

from services import UsersService


service = UsersService()
router = APIRouter(prefix='/users')


@router.get('/')
def users():
    s = service.get_users()
    return s
