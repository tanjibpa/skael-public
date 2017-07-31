"""Added kw-ds view

Revision ID: a2b117901ea6
Revises: b87a389fe98d
Create Date: 2017-07-11 23:43:04.085658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2b117901ea6'
down_revision = 'b87a389fe98d'
branch_labels = None
depends_on = None


def upgrade():
	sql = """
		CREATE VIEW kw_ds AS
			(SELECT ne.name ne_tag, kw.name keyword, ds.url dataSource
				FROM Keyword kw
				JOIN Keyword_NE_tag kw_ne ON kw_ne.keyword = kw.Id
				JOIN NE_tag ne ON ne.Id = kw_ne.ne_tag
				JOIN KeyWord_DataSource kwds ON kwds.keyword = kw.Id
				JOIN DataSource ds ON ds.id = kwds.datasource);
    """
	op.execute(sql)
	
	sql = """
		CREATE OR REPLACE FUNCTION insert_kw_ds()
		RETURNS TRIGGER
		LANGUAGE plpgsql
		AS $function$
			DECLARE
				ne_tag_id INT;
				kw_id INT;
				ds_id INT;
		BEGIN
			SELECT Id INTO ne_tag_id FROM NE_tag WHERE name = NEW.ne_tag;
			if ne_tag_id IS NULL THEN
				INSERT INTO NE_tag(name) VALUES(NEW.ne_tag) RETURNING Id INTO ne_tag_id;
			END IF;
				
			SELECT Id INTO kw_id FROM Keyword WHERE name = NEW.keyword;
			IF kw_id IS NULL THEN
				INSERT INTO Keyword(name) VALUES(NEW.keyword) RETURNING Id INTO kw_id;
			END IF;
			
			IF NOT EXISTS (SELECT 0 FROM KeyWord_NE_Tag WHERE keyword=kw_id AND NE_Tag=ne_tag_id) THEN
				INSERT INTO KeyWord_NE_Tag(keyword, NE_Tag) VALUES (kw_id, ne_tag_id);
			END IF;
		  
			SELECT Id INTO ds_id FROM DataSource where url = NEW.dataSource;
			IF ds_id IS NULL THEN
				INSERT INTO DataSource(url) VALUES(NEW.dataSource) RETURNING Id INTO ds_id;
			END IF;
				
			IF NOT EXISTS (SELECT 0 FROM KeyWord_DataSource WHERE keyword=kw_id AND datasource=ds_id) THEN
				INSERT INTO KeyWord_DataSource(keyword, datasource) VALUES (kw_id, ds_id);
			END IF;
		  
			RETURN NEW;
		END;
		$function$;
    """
	op.execute(sql)
	
	sql = "DROP TRIGGER IF EXISTS kw_ds_insert_trgr ON kw_ds"
	op.execute(sql)
	
	sql = """
		CREATE TRIGGER kw_ds_insert_trgr
		INSTEAD OF INSERT ON kw_ds 
        FOR EACH ROW EXECUTE PROCEDURE insert_kw_ds()
    """
	op.execute(sql)
	
	

def downgrade():
	sql = "DROP VIEW kw_ds"
	op.execute(sql)
	sql = "DROP FUNCTION IF EXISTS insert_kw_ds()"
	op.execute(sql)
