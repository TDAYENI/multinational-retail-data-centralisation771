import yaml
import psycopg2
from sqlalchemy import create_engine
# Todo which you will use to connect with and upload data to the database


class DataConnector:
    def __init__(self):
        self.db_cred = None


    def read_db_creds(self, cred_file_path):
        # reads database credentials then initaites method to create db connection
        with open(cred_file_path, 'r') as file:
            self.db_cred = yaml.safe_load(file)
        return self.init_db_engine(self.db_cred)
    
    def init_db_engine(self, db_cred):
        # return an sqlalchemy database engine
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2' 
        alchemy_engine = create_engine(
            f"{DATABASE_TYPE}+{DBAPI}://{db_cred['RDS_USER']}:"
            f"{db_cred['RDS_PASSWORD']}@{db_cred['RDS_HOST']}:"
            f"{db_cred['RDS_PORT']}/{db_cred['RDS_DATABASE']}"
            )
        print(alchemy_engine)
        return alchemy_engine
    

    def list_db_tables (self):
        inspector = inspect(engine)
        return(print(inspector.get_table_names()))


inst_connect = DataConnector()
inst_connect.read_db_creds('cred/db_creds.yaml')


