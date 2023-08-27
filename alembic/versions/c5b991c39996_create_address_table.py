"""Create address table

Revision ID: c5b991c39996
Revises: 83fa7c889ee4
Create Date: 2023-08-27 15:48:51.559693

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5b991c39996'
down_revision: Union[str, None] = '83fa7c889ee4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(100), nullable=False),
                    sa.Column('address2', sa.String(100), nullable=False),
                    sa.Column('city', sa.String(50), nullable=False),
                    sa.Column('state', sa.String(50), nullable=False),
                    sa.Column('country', sa.String(30), nullable=False),
                    sa.Column('postalcode', sa.String(20), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('address')
