"""Initial migration

Revision ID: 0ff16b4e250f
Revises: 
Create Date: 2025-07-26 22:14:13.860463
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0ff16b4e250f'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create the 'student' table
    op.create_table(
        'student',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uid', sa.String(length=100), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uid')
    )

    # Create the 'attendance' table
    op.create_table(
        'attendance',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('date', sa.String(length=10), nullable=False),
        sa.Column('status', sa.String(length=1), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='CASCADE')
    )

def downgrade():
    # Drop the tables in reverse order to respect foreign key constraints
    op.drop_table('attendance')
    op.drop_table('student')
