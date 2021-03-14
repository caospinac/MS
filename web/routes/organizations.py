from fastapi import APIRouter

from services import OrganizationsService
from schemas.organization import CreateSchema

service = OrganizationsService()
router = APIRouter(prefix='/organizations')


@router.get('/')
def get():
    s = service.get_organizations()
    return s


@router.post('/')
def create(payload: CreateSchema):
    result = service.create(payload)
    return result
