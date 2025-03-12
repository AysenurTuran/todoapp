"""phone number added

Revision ID: 3e8e85f56942
Revises: 
Create Date: 2025-03-12 11:18:59.610173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e8e85f56942'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """op.add_column('users', sa.Column('phone_number', sa.String(length=10), nullable=True))"""
    pass


def downgrade() -> None:
    pass

