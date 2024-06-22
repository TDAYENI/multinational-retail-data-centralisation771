import yaml
# Todo which you will use to connect with and upload data to the database


class DataConnector:
    def read_db_creds():
        with open('cred/db_creds.yaml') as file:
            db_cred = yaml.safe_load(file)
        return db_cred


inst_connect = DataConnector.read_db_creds()
print(inst_connect)
