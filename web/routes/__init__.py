from fastapi import APIRouter

from .users import router as usersRouter

router = APIRouter(prefix='/v1')
router.include_router(usersRouter)
