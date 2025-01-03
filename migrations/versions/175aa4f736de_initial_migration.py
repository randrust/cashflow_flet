"""Initial migration

Revision ID: 175aa4f736de
Revises: 
Create Date: 2024-12-15 12:58:37.609715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '175aa4f736de'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('c_id', sa.Integer(), nullable=False),
    sa.Column('c_name', sa.String(), nullable=True),
    sa.Column('c_short_name', sa.String(), nullable=True),
    sa.Column('c_is_main', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('c_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currencies')
    # ### end Alembic commands ###
