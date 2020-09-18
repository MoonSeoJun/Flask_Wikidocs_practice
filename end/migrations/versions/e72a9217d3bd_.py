"""empty message

Revision ID: e72a9217d3bd
Revises: f5dd039726b8
Create Date: 2020-09-16 18:40:28.742946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e72a9217d3bd'
down_revision = 'f5dd039726b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###