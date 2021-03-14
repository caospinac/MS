from fastapi import APIRouter

from .users import router as usersRouter
from .organizations import router as organizationsRouter

router = APIRouter(prefix='/v1')
router.include_router(usersRouter)
router.include_router(organizationsRouter)
