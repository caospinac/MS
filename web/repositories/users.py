from models import User
from repositories._utils import Repository, db_access


class UsersRepository(Repository):

    def get_model(self):
        return User

    @db_access
    def get_users(self, skip: int = 0, limit: int = 100):
        return self.query.offset(skip).limit(limit).all()
