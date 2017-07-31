# Skael 

## NLP

NLTK based keyword extractor initially trained by samples from Excel file

### Principal steps for native Python (Luigiless) execution.

* Excel file population. This step is executed manually. For incremental population, the same file can be freely updated, or more than one Excel files can be used independently. Any data duplication on single Excel file or between several files is safe, it will be programmatically checked-up and safely handled on subsequent steps.
Excel file must contain:
  * one or multiple columns containing comma-separated keywords, and 	
  * single column referencing data sources where keywords are from. Order of columns is not principal.

First row must contain names of NE categories e.g. "Equipment_interface", "Industry Terminology", etc. Space chars in category names will be forcibly replaced with underscores on subsequent steps for proper IOB tagging. These names are used to populate KeyWord_NE_tag SQL table. 

*  Porting of training data from Excel file(s) to SQL DB. This step is implemented programmatically on Python layer. Keywords ported from Excel file are approved automatically. It's safe to execute this step as many times as necessary.
  ```
  python3 excel2sql_keyword_porting.py <Excel workbook> 
		<data source column> 
		<SQL DB connection string> 
		<keyword column> [, <keyword column>...]
  ```
  ```
  Command line example:
	python excel2sql_keyword_porting.py keyword_samples/keyword_samples.xlsx 6 "postgresql://postgres:postgres@somehost/Skael" 0 1 2 3 4 5 7 8 9
  ```
  

* Keyword approvals on SQL layer. This step is executed manually after every SQL DB population event from any source except population by excel2sql_keyword_porting.py from Excel workbook. Query example:
   ```
   UPDATE Keyword SET approved = True;
   ```
   * NOTE: For data safety reasons keywords must be reviewed before approvals.

* Training corpora generation. This step is executed programmatically on Python layer. Command line format and example:
   ```
   python training_data_generation/sql_training_data_generator.py <SQL DB connection string>
   ```
   ```
   python training_data_generation/sql_training_data_generator.py "postgresql://postgres:postgres@localhost/Skael"
   ```

The generator creates as many tagged training corpuses as many entries there are on NE_Tag SQL table. Every new training corpora is added to NLP_Model table. Previous content of this table remains unchanged.
If necessary, for review reasons, etc., actual training corpora can be queried in this way:
	WITH LastCorpora AS (
        SELECT ne_tag, max(id) Id FROM nlp_Model GROUP BY ne_tag
    )
    SELECT net.name ne_tag, m.model
        FROM LastCorpora lc
        JOIN nlp_model m ON m.Id = lc.id
        JOIN ne_tag net on net.id = m.ne_tag;

* Keyword scrapping

python keyword_extractor.py <url> -s <SQL DB connection string> 
	
url - a link to web page to extract keywords from

The keyword_extractor always uses the most recent training corpora from Nlp_Model table.
The keyword_extractor submits new keywords to SQL DB.

## Examples:

python keyword_extractor.py  
	-s "postgresql://postgres:postgres@localhost/Skael"
	 "http://www.cisco.com/c/en/us/products/collateral/wireless/2500-series-wireless-controllers/data_sheet_c78-645111.html"

python keyword_extractor.py "http://www.cisco.com/c/en/us/products/collateral/wireless/2500-series-wireless-controllers/data_sheet_c78-645111.html"

python keyword_extractor.py "http://www.dlink.ru/ru/products/4/355.html"


** Principal steps for luigi based execution.
Luigi based execution consists of the same steps as luigiless one considered above. However these steps are executed under luigi scheduler.

## 2.1. This luigi step includes native steps 1.2 and 1.3. Command line format:
python excel2sql_keyword_porting_luigi.py Excel2SQL 
	[--local-scheduler]
	[--help]
	[--help-all]
	--ExcelBook-file <Excel book>
	--sql-connection <sql connection string>
	--url-column <column number 0,1,2....>
	--keyword-columns [column list]

An example:
python excel2sql_keyword_porting_luigi.py Excel2SQL --ExcelBook-file "Updated by Farooq Jul 11 2017 Keywords URL.xlsx" --url-column 6 --keyword-columns [0,1,2,3,4,5,7,8,9]



** Obsolete, deprecated and removed features:

##	NLP Model (tagged training corpora) is kept on local files.

## NLP Model file generation directly from excel file

	python excel_training_data_generator.py <excel file> <model file>

## NLP Model file generation example:

	python excel_training_data_generator.py "Keywords URL.xlsx" keyword.tags




