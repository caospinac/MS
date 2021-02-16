import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from . import Model


class CustomValue(Model):

    __tablename__ = 'custom_values'

    custom_field_id = sa.Column(UUID, sa.ForeignKey('custom_fields.id'),
                                nullable=False)
    custom_field = relationship('CustomField', back_populates='custom_values')
    entity_id = sa.Column(sa.String, nullable=False)
    value = sa.Column(sa.String)
