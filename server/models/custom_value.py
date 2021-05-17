import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ._utils import Model


class CustomValue(Model):

    __tablename__ = 'custom_values'

    custom_field_id = sa.Column(UUID(as_uuid=True),
                                sa.ForeignKey('custom_fields.id'),
                                nullable=False)
    entity_id = sa.Column(sa.String, nullable=False)
    value = sa.Column(sa.String)

    custom_field = relationship('CustomField', back_populates='custom_values')
