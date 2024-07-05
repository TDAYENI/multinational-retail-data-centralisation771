

from sqlalchemy import inspect
from sqlalchemy import text
import pandas as pd

# Todo The methods contained will be fit to extract data from a particular data source,
# Todo these sources will include CSV files, an API and an S3 bucket

class DataExtractor:
    def __init__(self):
        pass
    # class to read the data from the RDS database

    def read_rds_table(self,table_name,engine):
        legacy_users = pd.read_sql_table(table_name, engine)
        return legacy_users, print(legacy_users)







        
    
    # Todo extract the database table to a pandas DataFrame
    #  TODO ke in an instance of your DatabaseConnector class and 
    # TODO the table name as an argument and return a pandas DataFrame.

