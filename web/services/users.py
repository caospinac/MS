from repositories import UsersRepository
from ._utils import Service


class UsersService(Service):

    def get_repository(self):
        return UsersRepository
