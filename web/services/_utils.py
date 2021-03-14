import abc

from repositories._utils import Repository


class Service(abc.ABC):
    repository: Repository

    def __init__(self):
        RepositoryClass = self.get_repository()
        self.repository = RepositoryClass()

    @abc.abstractmethod
    def get_repository(self):
        pass
