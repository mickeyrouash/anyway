"""remove unecessary table index

Revision ID: 7574885e1fed
Revises: 98ad75de45b2
Create Date: 2020-01-15 05:43:48.413248

"""

# revision identifiers, used by Alembic.
revision = '7574885e1fed'
down_revision = '98ad75de45b2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('acc_long_lat_idx', table_name='markers')
    op.drop_index('provider_and_id_idx_markers', table_name='markers')
    op.drop_index('provider_and_id_idx_involved', table_name='involved')
    op.drop_index('provider_and_id_idx_vehicles', table_name='vehicles')
    op.drop_index('geom_gix', table_name='markers')
    op.drop_index('discussions_gix', table_name='discussions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('acc_long_lat_idx', 'markers', ['latitude', 'longitude'], unique=False)
    op.create_index('provider_and_id_idx_markers', 'markers', ['provider_and_id'], unique=False)
    op.create_index('provider_and_id_idx_involved', 'involved', ['provider_and_id'], unique=False)
    op.create_index('provider_and_id_idx_vehicles', 'vehicles', ['provider_and_id'], unique=False)
    conn.execute('CREATE INDEX geom_gix ON markers USING GIST (geography(geom));')
    conn.execute('CREATE INDEX discussions_gix ON discussions USING GIST (geography(geom));')
    # ### end Alembic commands ###