import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ._utils import Model


class Role(Model):

    __tablename__ = 'roles'

    name = sa.Column(sa.String, nullable=False)
    code = sa.Column(sa.String, nullable=False)
    organization_id = sa.Column(UUID, sa.ForeignKey('organizations.id'),
                                nullable=False)

    organization = relationship('Organization', back_populates='roles')
    users = relationship('User', back_populates='role')
