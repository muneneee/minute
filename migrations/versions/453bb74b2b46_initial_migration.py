"""Initial Migration

Revision ID: 453bb74b2b46
Revises: c34cc30251a2
Create Date: 2020-05-03 16:04:36.072743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '453bb74b2b46'
down_revision = 'c34cc30251a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
