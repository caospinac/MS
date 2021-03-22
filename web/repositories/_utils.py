import abc
import functools

from sqlalchemy.orm import Session, Query

from db import engine
from models._utils import Model


def db_access(handler):

    @functools.wraps(handler)
    def wrapper(instance, *args, **kwargs):
        instance.session = Session(bind=engine)
        instance.query = instance.session.query(instance.get_model())
        result = handler(instance, *args, **kwargs)
        instance.query = None
        instance.session.close()

        return result

    return wrapper


class Repository(abc.ABC):
    query: Query = None
    session: Session = None

    def add(self, instance):
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)

        return instance

    @abc.abstractmethod
    def get_model(self) -> Model:
        pass

    @db_access
    def get_all(self, skip: int = 0, limit: int = 100):
        return self.query.offset(skip).limit(limit).all()

    @db_access
    def get_by_id(self, ident):
        return self.query.get(ident)
