
from database_utils import DatabaseConnector
# Todo The methods contained will be fit to extract data from a particular data source,
# Todo these sources will include CSV files, an API and an S3 bucket

class DataExtractor:
    def __init__(self, db_connector):
    # class to read the data from the RDS database

    def read_rds_table(self,table_name):
        engine = DatabaseConnector()
        return df
    # Todo extract the database table to a pandas DataFrame
    #  TODO ke in an instance of your DatabaseConnector class and 
    # TODO the table name as an argument and return a pandas DataFrame.

