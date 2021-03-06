"""entries table

Revision ID: 6cf2e8c31643
Revises: 
Create Date: 2020-09-16 21:35:19.479380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6cf2e8c31643'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('fk_vehicle', sa.Integer(), nullable=False),
    sa.Column('fk_period', sa.Integer(), nullable=False),
    sa.Column('initial_hour', sa.Integer(), nullable=True),
    sa.Column('final_hour', sa.Integer(), nullable=True),
    sa.Column('hour_quantity', sa.Float(), nullable=False),
    sa.Column('total_value', sa.Float(), nullable=False),
    sa.Column('order_date', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),

    sa.PrimaryKeyConstraint('order_id')
    )
    period_table = op.create_table('period',
    sa.Column('period_id', sa.Integer(), nullable=False),
    sa.Column('initial_day', sa.Integer(), nullable=False),
    sa.Column('final_day', sa.Integer(), nullable=False),
    sa.Column('initial_hour', sa.Integer(), nullable=False),
    sa.Column('final_hour', sa.Integer(), nullable=False),
    sa.Column('value_per_hour', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('period_id')
    )



    # 5557 all images muras 


    vehicle = op.create_table('vehicle',
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.Column('vehicle_license_plate', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('vehicle_id')
    )

    op.bulk_insert(vehicle,
        [
             {'vehicle_license_plate':'rrr7871'},
             {'vehicle_license_plate':'qqq7871'}
        ],
        multiinsert=False
    )


    op.bulk_insert(period_table,
        [
             {
                'initial_day': 0,
                'final_day': 4,
                'initial_hour': 800,
                'final_hour': 1200,
                'value_per_hour': 2.00
                },
                {
                'initial_day': 0,
                'final_day': 4,
                'initial_hour': 1201,
                'final_hour': 1800,
                'value_per_hour': 3.00
                },
                {
                'initial_day': 5,
                'final_day': 6,
                'initial_hour': 800,
                'final_hour': 1800,
                'value_per_hour': 2.50
                }                
        ],
        multiinsert=False
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    op.drop_table('products')
    op.drop_table('period')
    op.drop_table('order')
    # ### end Alembic commands ###
