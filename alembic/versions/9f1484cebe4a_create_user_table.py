"""create user table

Revision ID: 9f1484cebe4a
Revises: 
Create Date: 2022-04-02 18:05:43.438082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f1484cebe4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('name', sa.String(150), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now())
    )


def downgrade():
    op.drop_table('users')
