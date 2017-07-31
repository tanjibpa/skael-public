"""Base migration. This migration houses the concept of a  user.
Revision ID: 98e29e2f0c84
Revises:
Create Date: 2017-06-25 21:51:05.010363
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98e29e2f0c84'
down_revision = 'a2b117901ea6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('public_id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('password', sa.Binary(), nullable=False),
    sa.Column('username', sa.Text(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('is_validated', sa.Boolean(), nullable=False),
    sa.Column('jwt_claim', sa.String(length=36), nullable=True),
    sa.Column('verify_token', sa.String(length=36), nullable=True),
    sa.Column('reset_token', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_jwt_claim'), 'users', ['jwt_claim'], unique=False)
    op.create_index(op.f('ix_users_public_id'), 'users', ['public_id'], unique=True)
    op.create_index(op.f('ix_users_reset_token'), 'users', ['reset_token'], unique=True)
    op.create_index(op.f('ix_users_verify_token'), 'users', ['verify_token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_verify_token'), table_name='users')
    op.drop_index(op.f('ix_users_reset_token'), table_name='users')
    op.drop_index(op.f('ix_users_public_id'), table_name='users')
    op.drop_index(op.f('ix_users_jwt_claim'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
