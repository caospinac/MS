import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from . import Model


class CustomField(Model):

    __tablename__ = 'custom_fields'

    organization_id = sa.Column(UUID, sa.ForeignKey('organizations.id'),
                                nullable=False)
    organization = relationship('Organization', back_populates='custom_fields')
    entity = sa.Column(sa.String, nullable=False)
    name = sa.Column(sa.String, nullable=False)
    type = sa.Column(sa.Enum('text', 'number', 'date', 'boolean'),
                     nullable=False, default='inactive')
    label = sa.Column(sa.String, nullable=False,
                      default=Model.default_value('name'))
    required = sa.Column(sa.Boolean, nullable=False, default=False)
    max_value = sa.Column(sa.Integer)
    min_value = sa.Column(sa.Integer)
    re_match = sa.Column(sa.String)
