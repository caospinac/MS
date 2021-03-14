from repositories import UsersRepository
from ._utils import Service


class UsersService(Service):

    def get_repository(self):
        return UsersRepository

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.repository.get_users(skip, limit)
