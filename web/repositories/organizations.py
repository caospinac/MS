from models import Organization
from repositories._utils import Repository, db_access


class OrganizationsRepository(Repository):

    def get_model(self):
        return Organization

    @db_access
    def get_by_prefix(self, prefix: str):
        return self.query.filter_by(prefix=prefix).one_or_none()
