from models import Role
from repositories._utils import Repository


class RolesRepository(Repository):

    def get_model(self):
        return Role
