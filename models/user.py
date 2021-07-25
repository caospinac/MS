import enum
from typing import TYPE_CHECKING, Type, TypeVar, Union

import bcrypt
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship, Session

from lib.const import DEFAULT_ROUNDS
from ._utils import Model


if TYPE_CHECKING:
    from . import Organization  # noqa: F401


class UserStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'
    unverified = 'unverified'


class UserRoles(enum.Enum):
    owner = 'owner'
    admin = 'admin'
    basic = 'basic'


T = TypeVar('T', bound='User')


class User(Model):

    STATUS_ACTIVE = UserStatus.active.value
    STATUS_INACTIVE = UserStatus.inactive.value
    STATUS_UNVERIFIED = UserStatus.unverified.value

    ROLE_OWNER = UserRoles.owner.value
    ROLE_ADMIN = UserRoles.admin.value
    ROLE_BASIC = UserRoles.basic.value

    __tablename__ = 'users'
    _repr_hide = ['password']

    external_id = sa.Column(sa.String, nullable=False,
                            default=Model.default_value('id'))
    status = sa.Column(sa.Enum(UserStatus),
                       nullable=False, default=STATUS_UNVERIFIED)
    role = sa.Column(sa.Enum(UserRoles),
                     nullable=False, default=ROLE_BASIC)
    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    phone_number = sa.Column(sa.String)
    avatar = sa.Column(sa.String)
    organization_id = sa.Column(PG_UUID(as_uuid=True),
                                sa.ForeignKey('organizations.id'),
                                nullable=False)

    organization = relationship('Organization', back_populates='users')

    @staticmethod
    def dummy_password_check() -> None:
        bcrypt.hashpw(b'', bcrypt.gensalt(rounds=DEFAULT_ROUNDS))

    def set_password(self, new_password: str) -> None:
        if not new_password:
            raise Exception('Passwords cannot be empty')

        salt = bcrypt.gensalt(rounds=DEFAULT_ROUNDS)
        password = bcrypt.hashpw(new_password.encode('utf-8'), salt)
        self.password = password.decode('utf-8')

    def check_password(self, plain_pw: str) -> bool:
        if not self.password:
            raise Exception('Password not set')

        return bcrypt.checkpw(plain_pw.encode('utf-8'),
                              self.password.encode('utf-8'))

    @classmethod
    def get_by_email(
        cls: Type[T], db: Session, oid: str, email: str,
    ) -> Union[T, None]:
        return db.query(cls)\
            .filter_by(organization_id=oid, email=email)\
            .one_or_none()

    @classmethod
    def get_by_external_id(
        cls: Type[T], db: Session, oid: str, external_id: str
    ) -> Union[T, None]:
        return db.query(cls)\
            .filter_by(organization_id=oid, external_id=external_id)\
            .one_or_none()
