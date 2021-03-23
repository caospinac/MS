import enum

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ._utils import Model


class UserStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'


class UserGender(enum.Enum):
    f = 'f'
    m = 'm'


class User(Model):

    __tablename__ = 'users'
    _repr_hide = ['password']

    external_id = sa.Column(sa.String, nullable=False,
                            default=Model.default_value('id'))
    status = sa.Column(sa.Enum(UserStatus),
                       nullable=False, default='inactive')
    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    birthdate = sa.Column(sa.Date)
    phone_number = sa.Column(sa.String)
    gender = sa.Column(sa.Enum(UserGender))
    avatar = sa.Column(sa.String)
    role_id = sa.Column(UUID(as_uuid=True), sa.ForeignKey('roles.id'),
                        nullable=False)

    role = relationship('Role', back_populates='users')
