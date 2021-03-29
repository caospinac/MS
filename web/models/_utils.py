import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session


Base = declarative_base()


class Model(Base):

    __abstract__ = True

    id = sa.Column(UUID(as_uuid=True), primary_key=True,
                   default=uuid.uuid4, unique=True, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now,
                           onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime, default=None)

    @staticmethod
    def default_value(column):
        return lambda cxt: cxt.get_current_parameters()[column]

    def save(self, db: Session, commit=True):
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

    def before_save(self, *args, **kwargs):
        pass

    def after_save(self, *args, **kwargs):
        pass

    def update(self, db: Session):
        self.before_update()
        db.commit()
        db.refresh(self)
        self.after_update()

    def before_update(self, *args, **kwargs):
        pass

    def after_update(self, *args, **kwargs):
        pass

    def delete(self, db: Session, logic=True, commit=True):
        db.delete(self)
        if logic:
            self.deleted_at = datetime.now()

        if commit:
            db.commit()

    @classmethod
    def restore(cls, db: Session, ident, commit=True):
        el: Model = db.query(cls).get(ident)
        el.deleted_at = None
        if commit:
            db.commit()
            db.refresh(el)

        return el

    @classmethod
    def get(cls, db: Session, ident):
        return db.query(cls).get(ident)

    @classmethod
    def get_list(cls, db: Session, *filters, skip: int = 0, limit: int = None):
        query = db.query(cls)
        for criteria in filters:
            query = query.filter(criteria)

        query = query.order_by(cls.created_at).offset(skip)
        if limit is not None:
            query = query.limit(limit)

        result = query.all()
        return result

    @classmethod
    def count(cls, db: Session):
        query = db.query(cls)

        return query.count()
