# type: ignore
'''create custom_fields

Revision ID: f65bf758ecbc
Revises: 40c6f3dc4c6d
Create Date: 2021-02-18 19:39:21.152864

'''
import enum
import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa

# pylint: disable=no-member
# revision identifiers, used by Alembic.
revision = 'f65bf758ecbc'
down_revision = '40c6f3dc4c6d'
branch_labels = None
depends_on = None


class CustomFieldType(enum.Enum):
    text = 'text'
    number = 'number'
    date = 'date'
    boolean = 'boolean'


def get_general_columns():
    return (
        sa.Column('id', UUID(as_uuid=True), primary_key=True,
                  default=uuid.uuid4, unique=True, nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at',
                  sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime, default=None),
    )


def upgrade():
    op.create_table(
        'custom_fields',
        *get_general_columns(),
        sa.Column('organization_id', UUID(as_uuid=True),
                  sa.ForeignKey('organizations.id')),
        sa.Column('entity', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('type', sa.Enum(CustomFieldType),
                  nullable=False, default='inactive'),
        sa.Column('label', sa.String, nullable=False),
        sa.Column('required', sa.Boolean, nullable=False, default=False),
        sa.Column('max_value', sa.Numeric),
        sa.Column('min_value', sa.Numeric),
        sa.Column('re_match', sa.String),
    )


def downgrade():
    op.drop_table('custom_fields')
    sa.Enum(CustomFieldType).drop(op.get_bind(), checkfirst=False)
