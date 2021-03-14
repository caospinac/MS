from repositories import OrganizationsRepository
from schemas.organization import CreateSchema
from ._utils import Service


class OrganizationsService(Service):

    def get_repository(self):
        return OrganizationsRepository

    def get_organizations(self, skip: int = 0, limit: int = 100):
        return self.repository.get_organizations(skip, limit)

    def create(self, payload: CreateSchema):
        result = self.repository.create(payload)
        return result
