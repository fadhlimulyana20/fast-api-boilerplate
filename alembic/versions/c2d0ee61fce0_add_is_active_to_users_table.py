"""Add is_active to users table

Revision ID: c2d0ee61fce0
Revises: 9f1484cebe4a
Create Date: 2022-04-03 03:01:20.214269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2d0ee61fce0'
down_revision = '9f1484cebe4a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('is_active', sa.Boolean))


def downgrade():
    op.drop_column('users', 'is_active')

