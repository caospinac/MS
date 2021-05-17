import enum

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ._utils import Model


class CustomFieldType(enum.Enum):
    text = 'text'
    number = 'number'
    date = 'date'
    boolean = 'boolean'


class CustomField(Model):

    TYPE_TEXT = CustomFieldType.text
    TYPE_NUMBER = CustomFieldType.number
    TYPE_DATE = CustomFieldType.date
    TYPE_BOOLEAN = CustomFieldType.boolean

    __tablename__ = 'custom_fields'

    organization_id = sa.Column(
        UUID(as_uuid=True), sa.ForeignKey('organizations.id'))
    entity = sa.Column(sa.String, nullable=False)
    name = sa.Column(sa.String, nullable=False)
    type = sa.Column(sa.Enum(CustomFieldType),
                     nullable=False, default='inactive')
    label = sa.Column(sa.String, nullable=False,
                      default=Model.default_value('name'))
    required = sa.Column(sa.Boolean, nullable=False, default=False)
    max_value = sa.Column(sa.Numeric)
    min_value = sa.Column(sa.Numeric)
    re_match = sa.Column(sa.String)

    organization = relationship('Organization', back_populates='custom_fields')
    custom_values = relationship('CustomValue', back_populates='custom_field')
