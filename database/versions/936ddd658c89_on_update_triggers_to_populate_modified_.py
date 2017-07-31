"""ON UPDATE triggers to populate modified_xx fields

Revision ID: 936ddd658c89
Revises: a2aa429abf05
Create Date: 2017-07-29 22:57:42.764368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936ddd658c89'
down_revision = 'a2aa429abf05'
branch_labels = None
depends_on = None


def upgrade():
	sql = """
		CREATE OR REPLACE FUNCTION set_modified_xx()
		RETURNS TRIGGER
		LANGUAGE plpgsql
		AS $function$
		BEGIN
			IF NEW.updated_on IS NULL THEN
				NEW.updated_on = now();
			END IF;
				
			IF NEW.updated_by IS NULL THEN
				NEW.updated_by = CURRENT_USER;
			END IF;
						  
			RETURN NEW;
		END;
		$function$;
    """
	op.execute(sql)
	
	sql = "DROP TRIGGER IF EXISTS Keyword_Update_trgr ON Keyword"
	op.execute(sql)
	
	sql = """
		CREATE TRIGGER Keyword_Update_trgr
		BEFORE UPDATE ON Keyword 
        FOR EACH ROW EXECUTE PROCEDURE set_modified_xx()
    """
	op.execute(sql)

	sql = "DROP TRIGGER IF EXISTS NE_tag_Update_trgr ON NE_tag"
	op.execute(sql)
	
	sql = """
		CREATE TRIGGER NE_tag_Update_trgr
		BEFORE UPDATE ON NE_tag 
        FOR EACH ROW EXECUTE PROCEDURE set_modified_xx()
    """
	op.execute(sql)

	sql = "DROP TRIGGER IF EXISTS NLP_Model_Update_trgr ON NLP_Model"
	op.execute(sql)
	
	sql = """
		CREATE TRIGGER NLP_Model_Update_trgr
		BEFORE UPDATE ON NLP_Model 
        FOR EACH ROW EXECUTE PROCEDURE set_modified_xx()
    """
	op.execute(sql)

	sql = "DROP TRIGGER IF EXISTS DataSource_Update_trgr ON DataSource"
	op.execute(sql)
	
	sql = """
		CREATE TRIGGER DataSource_Update_trgr
		BEFORE UPDATE ON DataSource 
        FOR EACH ROW EXECUTE PROCEDURE set_modified_xx()
    """
	op.execute(sql)


def downgrade():
	sql = "DROP TRIGGER IF EXISTS Keyword_Update_trgr ON Keyword"
	op.execute(sql)
	sql = "DROP TRIGGER IF EXISTS NE_tag_Update_trgr ON NE_tag"
	op.execute(sql)
	sql = "DROP TRIGGER IF EXISTS NLP_Model_Update_trgr ON NLP_Model"
	op.execute(sql)
	sql = "DROP TRIGGER IF EXISTS DataSource_Update_trgr ON DataSource"
	op.execute(sql)
	sql = "DROP FUNCTION IF EXISTS set_modified_xx()"
	op.execute(sql)
