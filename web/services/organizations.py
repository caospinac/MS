from fastapi import HTTPException

from repositories import OrganizationsRepository
from schemas.organization import CreateSchema
from ._utils import Service


class OrganizationsService(Service):

    def get_repository(self):
        return OrganizationsRepository

    def create(self, payload: CreateSchema):
        existing_org = self.repository.get_by_prefix(payload.prefix)
        if existing_org:
            raise HTTPException(400, 'Prefix not available')

        result = self.repository.create(payload)
        return result
