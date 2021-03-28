import enum

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Session

from ._utils import Model


class OrganizationStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'


class Organization(Model):

    __tablename__ = 'organizations'

    name = sa.Column(sa.String, nullable=False)
    logo = sa.Column(sa.String)
    prefix = sa.Column(sa.String, nullable=False, unique=True)
    status = sa.Column(sa.Enum(OrganizationStatus),
                       nullable=False, default='inactive')

    users = relationship('User', back_populates='organization')
    roles = relationship('Role', back_populates='organization')
    custom_fields = relationship('CustomField', back_populates='organization')

    @classmethod
    def get_by_prefix(cls, db: Session, prefix: str):
        return db.query(cls).filter_by(prefix=prefix).one_or_none()
