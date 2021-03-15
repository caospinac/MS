from repositories import OrganizationsRepository
from schemas.organization import CreateSchema
from ._utils import Service


class OrganizationsService(Service):

    def get_repository(self):
        return OrganizationsRepository

    def get_organizations(self, **kwargs):
        return self.repository.get_organizations(**kwargs)

    def create(self, payload: CreateSchema):
        result = self.repository.create(payload)
        return result
