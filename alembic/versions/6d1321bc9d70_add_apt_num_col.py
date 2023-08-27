"""add apt num col

Revision ID: 6d1321bc9d70
Revises: 76b3ffe59dd8
Create Date: 2023-08-27 16:37:45.949916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d1321bc9d70'
down_revision: Union[str, None] = '76b3ffe59dd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("address", sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
