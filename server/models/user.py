import enum

import bcrypt
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Session

from lib.const import DEFAULT_ROUNDS
from ._utils import Model


class UserStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'
    unverified = 'unverified'


class UserRoles(enum.Enum):
    owner = 'owner'
    admin = 'admin'
    basic = 'basic'


class User(Model):

    STATUS_ACTIVE = UserStatus.active
    STATUS_INACTIVE = UserStatus.inactive
    STATUS_UNVERIFIED = UserStatus.unverified

    ROLE_OWNER = UserRoles.owner
    ROLE_ADMIN = UserRoles.admin
    ROLE_BASIC = UserRoles.basic

    __tablename__ = 'users'
    _repr_hide = ['password']

    external_id = sa.Column(sa.String, nullable=False,
                            default=Model.default_value('id'))
    status = sa.Column(sa.Enum(UserStatus),
                       nullable=False, default=UserStatus.unverified)
    role = sa.Column(sa.Enum(UserRoles),
                     nullable=False, default=UserRoles.basic)
    email = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    phone_number = sa.Column(sa.String)
    avatar = sa.Column(sa.String)
    organization_id = sa.Column(UUID(as_uuid=True),
                                sa.ForeignKey('organizations.id'),
                                nullable=False)

    organization = relationship('Organization', back_populates='users')

    @staticmethod
    def dummy_password_check():
        bcrypt.hashpw(b'', bcrypt.gensalt(rounds=DEFAULT_ROUNDS))

    def set_password(self, new_password: str):
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
    def get_by_email(cls, db: Session, oid: str, email: str):
        result: cls = db.query(cls)\
            .filter_by(organization_id=oid, email=email)\
            .one_or_none()

        return result

    @classmethod
    def get_by_external_id(cls, db: Session, oid: str, external_id: str):
        result: cls = db.query(cls)\
            .filter_by(organization_id=oid, external_id=external_id)\
            .one_or_none()

        return result
