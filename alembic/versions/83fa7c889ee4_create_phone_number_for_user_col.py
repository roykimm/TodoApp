"""create phone number for user col

Revision ID: 83fa7c889ee4
Revises: 
Create Date: 2023-08-27 15:37:27.564991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83fa7c889ee4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column('phone_number', sa.String(10), nullable=True))


def downgrade() -> None:
    op.drop_column("users", 'phone_number')
