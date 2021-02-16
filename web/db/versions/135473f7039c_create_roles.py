"""create roles

Revision ID: 135473f7039c
Revises: a591bc267bc6
Create Date: 2021-02-14 15:59:44.517294

"""
import uuid
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# pylint: disable=no-member
# revision identifiers, used by Alembic.
revision = '135473f7039c'
down_revision = 'a591bc267bc6'
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
        'roles',
        *get_general_columns(),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('code', sa.String, nullable=False),
        sa.Column('organization_id', UUID, sa.ForeignKey('organizations.id'),
                  nullable=False)
    )


def downgrade():
    op.drop_table('roles')
