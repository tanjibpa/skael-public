"""store models in SQL DB instead of local files

Revision ID: a2aa429abf05
Revises: ea67e41a02bd
Create Date: 2017-07-28 19:59:04.647304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2aa429abf05'
down_revision = 'ea67e41a02bd'
branch_labels = None
depends_on = None


def upgrade():
	sql = """
		ALTER TABLE nlp_model DROP CONSTRAINT nlp_model_url_key;
    """
	op.execute(sql)

	sql = """
		ALTER TABLE nlp_model DROP COLUMN url;
    """
	op.execute(sql)

	sql = """
		ALTER TABLE nlp_model ADD COLUMN model TEXT NOT NULL;
    """
	op.execute(sql)


def downgrade():
	sql = """
		ALTER TABLE nlp_model DROP COLUMN model Text;
    """
	op.execute(sql)

	sql = """
		ALTER TABLE nlp_model ADD COLUMN url VARCHAR(1024) NOT NULL;
    """
	op.execute(sql)

	sql = """
		ALTER TABLE nlp_model ADD CONSTRAINT nlp_model_url_key UNIQUE(url);
    """
	op.execute(sql)

