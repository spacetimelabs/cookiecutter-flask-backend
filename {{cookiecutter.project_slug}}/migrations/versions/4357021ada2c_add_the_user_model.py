"""Add the User model

Revision ID: 4357021ada2c
Revises: 
Create Date: 2020-04-07 16:12:08.520751

"""
from alembic import op
import sqlalchemy as sa


revision = '4357021ada2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.String(length=128), nullable=True),
        sa.Column('password', sa.String(length=512), nullable=True),
        sa.Column('first_name', sa.String(length=32), nullable=True),
        sa.Column('last_name', sa.String(length=64), nullable=True),
        sa.Column('email', sa.String(length=128), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('user')
