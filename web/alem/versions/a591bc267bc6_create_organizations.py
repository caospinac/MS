"""create organizations

Revision ID: a591bc267bc6
Revises:
Create Date: 2021-02-13 17:17:59.536990

"""
import enum
import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa


# pylint: disable=no-member
# revision identifiers, used by Alembic.
revision = 'a591bc267bc6'
down_revision = None
branch_labels = None
depends_on = None


class OrganizationStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'


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
        'organizations',
        *get_general_columns(),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('logo', sa.String),
        sa.Column('prefix', sa.String, nullable=False, unique=True),
        sa.Column('status', sa.Enum(OrganizationStatus),
                  nullable=False, default='inactive'),
    )


def downgrade():
    op.drop_table('organizations')
    sa.Enum(OrganizationStatus).drop(op.get_bind(), checkfirst=False)
