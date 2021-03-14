from fastapi import APIRouter

from repositories import UsersRepository


r = UsersRepository()
router = APIRouter(prefix='/users')


@router.get('/')
def users():
    s = r.get_users()
    return s
