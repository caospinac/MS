import enum

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import Model


class OrganizationStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'

class Organization(Model):

    __tablename__ = 'organizations'

    name = sa.Column(sa.String, nullable=False)
    logo = sa.Column(sa.String)
    prefix = sa.Column(sa.String, nullable=False, unique=True)
    users = relationship('User', back_populates='organization')
    status = sa.Column(sa.Enum(OrganizationStatus),
                    nullable=False, default='inactive')
