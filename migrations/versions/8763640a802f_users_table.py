"""users table

Revision ID: 8763640a802f
Revises: 
Create Date: 2018-02-13 22:39:09.976805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8763640a802f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=True),
    sa.Column('subscribed', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###