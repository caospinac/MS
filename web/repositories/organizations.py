from models import Organization
from repositories._utils import Repository, db_access
from schemas.organization import CreateSchema


class OrganizationsRepository(Repository):

    def get_model(self):
        return Organization

    @db_access
    def create(self, payload: CreateSchema):
        new = Organization(name=payload.name, prefix=payload.prefix)
        self.add(new)
        return new.id

    @db_access
    def get_organizations(self, skip: int = 0, limit: int = 100):
        return self.query.offset(skip).limit(limit).all()
