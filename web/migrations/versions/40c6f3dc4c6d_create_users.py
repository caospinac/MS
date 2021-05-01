"""create users

Revision ID: 40c6f3dc4c6d
Revises: a591bc267bc6
Create Date: 2021-02-17 18:49:35.559357

"""
import enum
import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa


# pylint: disable=no-member
# revision identifiers, used by Alembic.
revision = '40c6f3dc4c6d'
down_revision = 'a591bc267bc6'
branch_labels = None
depends_on = None


class UserStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'
    unverified = 'unverified'


class UserRoles(enum.Enum):
    owner = 'owner'
    admin = 'admin'
    basic = 'basic'


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
        'users',
        *get_general_columns(),
        sa.Column('external_id', sa.String, nullable=False),
        sa.Column('status', sa.Enum(UserStatus), nullable=False,
                  default=UserStatus.unverified),
        sa.Column('role', sa.Enum(UserRoles), nullable=False,
                  default=UserRoles.basic),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('phone_number', sa.String),
        sa.Column('avatar', sa.String),
        sa.Column('organization_id', UUID(as_uuid=True),
                  sa.ForeignKey('organizations.id'), nullable=False),
    )


def downgrade():
    op.drop_table('users')
    sa.Enum(UserStatus).drop(op.get_bind(), checkfirst=False)
    sa.Enum(UserRoles).drop(op.get_bind(), checkfirst=False)
