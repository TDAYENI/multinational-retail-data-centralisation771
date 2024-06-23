import yaml
# Todo which you will use to connect with and upload data to the database


class DataConnector:

    def read_db_creds(self, cred_file_path):

        with open(cred_file_path, 'r') as file:
            db_cred = yaml.safe_load(file)
        return self.init_db_engine(db_cred)
    
    def init_db_engine(self, db_cred):
        DATABASE_TYPE = 'postgresql'
        # DBAPI = 'psycopg2'
        # ENDPOINT = "<your-amazon-rds-endpoint>"
        # USER = 'postgres'
        # PASSWORD = "<your-password>"
        # PORT = 5432
        # DATABASE = 'postgres
        print(self.read_db_creds)


inst_connect = DataConnector('cred/db_creds.yaml')


