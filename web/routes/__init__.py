from fastapi import APIRouter

from .auth import router as authRouter
from .users import router as usersRouter
from .organizations import router as organizationsRouter


router = APIRouter()


@router.get('/health')
async def read_root():
    return 'OK'


router.include_router(authRouter)
router.include_router(usersRouter)
router.include_router(organizationsRouter)
