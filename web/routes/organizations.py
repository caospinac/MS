from fastapi import APIRouter

from repositories import OrganizationsRepository
from schemas.organization import CreateSchema

r = OrganizationsRepository()
router = APIRouter(prefix='/organizations')


@router.get('/')
def get():
    s = r.get_organizations()
    return s


@router.post('/')
def create(payload: CreateSchema):
    result = r.create_organizations(payload)
    return result
