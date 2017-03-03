"""Ensuring we have endpoint updated times and certificate rotation availability.

Revision ID: 131ec6accff5
Revises: e3691fc396e9
Create Date: 2016-12-07 17:29:42.049986

"""

# revision identifiers, used by Alembic.
revision = '131ec6accff5'
down_revision = 'e3691fc396e9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('certificates', sa.Column('rotation', sa.Boolean(), nullable=False, server_default=False))
    op.add_column('endpoints', sa.Column('last_updated', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('endpoints', 'last_updated')
    op.drop_column('certificates', 'rotation')
    # ### end Alembic commands ###
