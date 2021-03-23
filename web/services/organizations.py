from fastapi import HTTPException

from repositories import OrganizationsRepository
from schemas.organization import CreateSchema
from ._utils import Service


class OrganizationsService(Service):

    def get_repository(self):
        return OrganizationsRepository

    def create(self, payload: CreateSchema):
        from models import Organization, Role, User

        existing_org = self.repository.get_by_prefix(payload.prefix)
        if existing_org:
            raise HTTPException(400, 'Prefix not available')

        organization = Organization(name=payload.name, prefix=payload.prefix)
        role = Role(code='owner')
        user = User(**payload.owner.__dict__)

        role.users.append(user)
        organization.roles.append(role)

        return self.repository.add(organization)
