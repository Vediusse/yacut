"""added added_by field

Revision ID: 9277b991ba99
Revises: 
Create Date: 2023-06-28 12:59:08.037525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9277b991ba99"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "url_map",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("original", sa.Text(), nullable=False),
        sa.Column("short", sa.String(length=128), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("short"),
    )
    op.create_index(
        op.f("ix_url_map_timestamp"), "url_map", ["timestamp"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_url_map_timestamp"), table_name="url_map")
    op.drop_table("url_map")
    # ### end Alembic commands ###