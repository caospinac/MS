import enum
from typing import TYPE_CHECKING, Type, TypeVar, Union

import sqlalchemy as sa
from sqlalchemy.orm import relationship, Session

from ._utils import Model

if TYPE_CHECKING:
    from . import User, CustomField  # noqa: F401


class OrganizationStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'


T = TypeVar('T', bound='Organization')


class Organization(Model):

    STATUS_ACTIVE = OrganizationStatus.active.value
    STATUS_INACTIVE = OrganizationStatus.inactive.value

    __tablename__ = 'organizations'

    name = sa.Column(sa.String, nullable=False)
    logo = sa.Column(sa.String)
    prefix = sa.Column(sa.String, nullable=False, unique=True)
    status = sa.Column(sa.Enum(OrganizationStatus),
                       nullable=False, default='inactive')

    users = relationship('User', back_populates='organization', uselist=True)
    custom_fields = relationship('CustomField', back_populates='organization',
                                 uselist=True)

    @classmethod
    def get_by_prefix(cls: Type[T], db: Session, prefix: str) -> Union[T, None]:
        return db.query(cls).filter_by(prefix=prefix).one_or_none()
