"""create custom_values

Revision ID: d7d080fe51ad
Revises: f65bf758ecbc
Create Date: 2021-02-18 19:52:21.138132

"""
import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa

# pylint: disable=no-member
# revision identifiers, used by Alembic.
revision = 'd7d080fe51ad'
down_revision = 'f65bf758ecbc'
branch_labels = None
depends_on = None


def get_general_columns():
    return (
        sa.Column('id', UUID, primary_key=True,
                  default=uuid.uuid4, unique=True, nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.now),
        sa.Column('updated_at',
                  sa.DateTime, default=datetime.now, onupdate=datetime.now),
        sa.Column('deleted_at', sa.DateTime, default=None),
    )


def upgrade():
    op.create_table(
        'custom_values',
        *get_general_columns(),
        sa.Column('custom_field_id',
                  UUID, sa.ForeignKey('custom_fields.id'), nullable=False),
        sa.Column('entity_id', sa.String, nullable=False),
        sa.Column('value', sa.String),
    )


def downgrade():
    op.drop_table('custom_values')
