"""update user

Revision ID: a154fc22fd61
Revises: d0d04c2130c5
Create Date: 2021-07-13 18:28:44.975314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a154fc22fd61'
down_revision = 'd0d04c2130c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=False, server_default=''))
        batch_op.add_column(sa.Column('surname', sa.String(length=100), nullable=False, server_default=''))
        batch_op.add_column(sa.Column('mid_name', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('passport', sa.Integer(), nullable=False, server_default='1234123456'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('passport')
        batch_op.drop_column('mid_name')
        batch_op.drop_column('surname')
        batch_op.drop_column('name')

    # ### end Alembic commands ###