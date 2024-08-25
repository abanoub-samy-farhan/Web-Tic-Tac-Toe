"""add the default filed to the create and update columns

Revision ID: 43a9ecb6e317
Revises: 4d6f0c98f1ee
Create Date: 2024-08-25 19:20:51.031129

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '43a9ecb6e317'
down_revision = '4d6f0c98f1ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
        batch_op.drop_column('upadted_at')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
        batch_op.drop_column('upadted_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('upadted_at', mysql.DATETIME(), nullable=False))
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.add_column(sa.Column('upadted_at', mysql.DATETIME(), nullable=False))
        batch_op.alter_column('created_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
