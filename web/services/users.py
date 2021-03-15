from repositories import UsersRepository
from ._utils import Service


class UsersService(Service):

    def get_repository(self):
        return UsersRepository

    def get_users(self, **kwargs):
        return self.repository.get_users(**kwargs)
