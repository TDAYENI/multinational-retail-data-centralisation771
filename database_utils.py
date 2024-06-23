import yaml
import psycopg2
from sqlalchemy import create_engine
# Todo which you will use to connect with and upload data to the database


class DataConnector:
    def __init__(self):
        self.db_cred = None

    def read_db_creds(self, cred_file_path):

        with open(cred_file_path, 'r') as file:
            self.db_cred = yaml.safe_load(file)
        return self.init_db_engine(self.db_cred)
    
    def init_db_engine(self, db_cred):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = db_cred['RDS_HOST']
        USER = db_cred['RDS_USER']
        PASSWORD = db_cred['RDS_PASSWORD']
        DATABASE = db_cred['RDS_DATABASE']
        PORT = db_cred['RDS_PORT']
        engine = create_engine(
            f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        print(engine)


inst_connect = DataConnector()
inst_connect.read_db_creds('cred/db_creds.yaml')


