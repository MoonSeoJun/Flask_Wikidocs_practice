"""empty message

Revision ID: 6c8d99f8338a
Revises: 4ac6297f38fc
Create Date: 2020-09-17 19:11:38.231026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c8d99f8338a'
down_revision = '4ac6297f38fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('modify')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify', sa.DATETIME(), nullable=True))
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
