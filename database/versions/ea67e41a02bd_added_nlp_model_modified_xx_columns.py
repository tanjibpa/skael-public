"""added nlp_model.Modified_XX columns

Revision ID: ea67e41a02bd
Revises: 98e29e2f0c84
Create Date: 2017-07-28 19:31:36.396144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea67e41a02bd'
down_revision = '98e29e2f0c84'
branch_labels = None
depends_on = None


def upgrade():
	sql = """
		ALTER TABLE nlp_model ADD COLUMN updated_on TIMESTAMP;
    """
	op.execute(sql)

	sql = """
		ALTER TABLE nlp_model ADD COLUMN updated_by VARCHAR(256);
    """
	op.execute(sql)


def downgrade():
	sql = """
		ALTER TABLE nlp_model DROP COLUMN updated_on;
    """
	op.execute(sql)

	sql = """
		ALTER TABLE nlp_model DROP COLUMN updated_by;
    """
	op.execute(sql)
