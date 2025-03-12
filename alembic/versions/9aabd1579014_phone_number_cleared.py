"""phone number cleared

Revision ID: 9aabd1579014
Revises: 3e8e85f56942
Create Date: 2025-03-12 11:46:24.517904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9aabd1579014'
down_revision: Union[str, None] = '3e8e85f56942'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')

