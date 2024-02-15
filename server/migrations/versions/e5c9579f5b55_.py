"""empty message

Revision ID: e5c9579f5b55
Revises: 5b08caf55dd2
Create Date: 2024-02-14 23:21:41.776531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5c9579f5b55'
down_revision = '5b08caf55dd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dog_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('day', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_routines')),
    sa.UniqueConstraint('dog_id', name=op.f('uq_routines_dog_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routines')
    # ### end Alembic commands ###
