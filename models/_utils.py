from typing import Any, List, Type, TypeVar, Union
import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Session


Base = declarative_base()
T = TypeVar('T', bound='Model')


class Model(Base):

    __abstract__ = True

    id = sa.Column(PG_UUID(as_uuid=True), primary_key=True,
                   default=uuid.uuid4, unique=True, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now,
                           onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime, default=None, nullable=True)

    @staticmethod
    def default_value(column: str) -> Any:
        return lambda cxt: cxt.get_current_parameters()[column]

    def save(self, db: Session, commit: bool = True) -> None:
        self.before_save()
        db.add(self)
        if commit:
            try:
                db.commit()
                db.refresh(self)
            except Exception as e:
                db.rollback()
                raise e

        self.after_save()

    def before_save(self, *args: Any, **kwargs: Any) -> None:
        pass

    def after_save(self, *args: Any, **kwargs: Any) -> None:
        pass

    def update(self, db: Session) -> None:
        self.before_update()
        db.commit()
        db.refresh(self)
        self.after_update()

    def before_update(self, *args: Any, **kwargs: Any) -> None:
        pass

    def after_update(self, *args: Any, **kwargs: Any) -> None:
        pass

    def delete(self, db: Session, logic: bool = True,
               commit: bool = True) -> None:
        if logic:
            self.deleted_at = datetime.now()
            if commit:
                db.commit()
                db.refresh(self)
        else:
            db.delete(self)

    @classmethod
    def restore(cls: Type[T], db: Session, ident: str,
                commit: bool = True) -> Union[T, None]:
        el = db.query(cls).get(ident)
        if el is None:
            return None

        el.deleted_at = None
        if commit:
            db.commit()
            db.refresh(el)

        return el

    @classmethod
    def get(
        cls: Type[T], db: Session, ident: str, include_deleted: bool = False,
    ) -> Union[T, None]:
        el = db.query(cls).get(ident)

        if el is None or include_deleted and el.deleted_at is not None:
            return None

        return el

    @classmethod
    def get_list(
        cls: Type[T], db: Session, *filters: Any, skip: int = 0,
        limit: int = None, include_deleted: bool = False,
    ) -> List[T]:
        query = db.query(cls)
        for criteria in filters:
            query = query.filter(criteria)

        if not include_deleted:
            query = query.filter_by(deleted_at=None)

        query = query.order_by(cls.created_at).offset(skip)
        if limit is not None:
            query = query.limit(limit)

        return query.all()

    @classmethod
    def count(
        cls: Type[T], db: Session, *filters: Any,
        include_deleted: bool = False,
    ) -> int:
        query = db.query(cls)
        if not include_deleted:
            query = query.filter_by(deleted_at=None)

        for criteria in filters:
            query = query.filter(criteria)

        return query.count()
