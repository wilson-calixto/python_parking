"""empty message

Revision ID: 00308915d778
Revises: 6cf2e8c31643
Create Date: 2020-09-17 16:37:53.313006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00308915d778'
down_revision = '6cf2e8c31643'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'order', 'vehicle', ['fk_vehicle'], ['vehicle_id'])
    op.create_foreign_key(None, 'order', 'period', ['fk_period'], ['period_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_constraint(None, 'order', type_='foreignkey')
    # ### end Alembic commands ###
