import yaml
# Todo which you will use to connect with and upload data to the database


class DataConnector:
    def __init__(self,cred_file_path):
        self.cred_file_path = cred_file_path
        self.db_cred = self.read_db_creds()


    def read_db_creds(self,):
        with open(self.cred_file_path, 'r') as file:
            db_cred = yaml.safe_load(file)
        return print(db_cred)
    
    def init_db_engine():
        pass


inst_connect = DataConnector('cred/db_creds.yaml')


