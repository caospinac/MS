from fastapi import APIRouter

from repositories import OrganizationsRepository


r = OrganizationsRepository()
router = APIRouter(prefix='/organizations')


@router.get('/')
def organizations():
    s = r.get_organizations()
    return s
