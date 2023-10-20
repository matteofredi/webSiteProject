"""init user table

Revision ID: dd8c2f5d5f7f
Revises: Matteo Fredi
Create Date: 2023-10-20 15:52:01.092708

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'dd8c2f5d5f7f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('username', sa.String(length=50), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('salt', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id', name='id_primary_key_constraint'),
                    sa.UniqueConstraint('hashed_password'),
                    sa.UniqueConstraint('salt'),
                    sa.UniqueConstraint('username')
                    )


def downgrade() -> None:
    op.drop_table('user')
