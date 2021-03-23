"""create users

Revision ID: 40c6f3dc4c6d
Revises: 135473f7039c
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
down_revision = '135473f7039c'
branch_labels = None
depends_on = None


class UserStatus(enum.Enum):
    active = 'active'
    inactive = 'inactive'


class UserGender(enum.Enum):
    f = 'f'
    m = 'm'


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
        'users',
        *get_general_columns(),
        sa.Column('external_id', sa.String, nullable=False),
        sa.Column('status', sa.Enum(UserStatus),
                  nullable=False, default='inactive'),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('birthdate', sa.Date),
        sa.Column('phone_number', sa.String),
        sa.Column('gender', sa.Enum(UserGender)),
        sa.Column('avatar', sa.String),
        sa.Column('role_id', UUID, sa.ForeignKey('roles.id'), nullable=False)
    )


def downgrade():
    op.drop_table('users')
    sa.Enum(UserStatus).drop(op.get_bind(), checkfirst=False)
    sa.Enum(UserGender).drop(op.get_bind(), checkfirst=False)
