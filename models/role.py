from typing import TYPE_CHECKING, Type, TypeVar, Union

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship, Session

from ._utils import Model

if TYPE_CHECKING:
    from . import Organization, User  # noqa: F401


T = TypeVar('T', bound='Role')


class Role(Model):

    CODE_DEFAULT = 'default'
    CODE_OWNER = 'owner'

    __tablename__ = 'roles'

    code = sa.Column(sa.String, nullable=False, default=CODE_DEFAULT)
    name = sa.Column(sa.String, nullable=False,
                     default=Model.default_value('code'))
    organization_id = sa.Column(PG_UUID(as_uuid=True),
                                sa.ForeignKey('organizations.id'),
                                nullable=False)

    organization = relationship('Organization', back_populates='roles')
    users = relationship('User', back_populates='role', uselist=True)

    @classmethod
    def get_by_code(
        cls: Type[T], db: Session, oid: str, code: str,
    ) -> Union[T, None]:
        return db.query(cls)\
            .filter_by(organization_id=oid, code=code)\
            .one_or_none()
