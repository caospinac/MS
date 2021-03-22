from models import User
from repositories._utils import Repository


class UsersRepository(Repository):

    def get_model(self):
        return User
