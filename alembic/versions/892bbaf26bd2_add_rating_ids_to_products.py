"""Add rating_ids to products

Revision ID: 892bbaf26bd2
Revises: 
Create Date: 2024-10-07 21:40:23.200580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '892bbaf26bd2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.add_column('products', sa.Column('rating_id', sa.ARRAY(sa.Integer()), nullable=True))

def downgrade():
    op.drop_column('products', 'rating_id')
