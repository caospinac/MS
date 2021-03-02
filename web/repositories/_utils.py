import abc
import functools

from sqlalchemy.orm import Session, Query

from db import engine
from models._utils import Model


class Repository(abc.ABC):
    query: Query = None

    @abc.abstractmethod
    def get_model(self) -> Model:
        pass


def db_access(handler):

    @functools.wraps(handler)
    def wrapper(instance: Repository, *args, **kwargs):
        session = Session(bind=engine)
        instance.query = session.query(instance.get_model())
        result = handler(instance, *args, **kwargs)
        instance.query = None
        session.close()

        return result

    return wrapper
