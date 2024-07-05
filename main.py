from data_extraction import DataExtractor
from database_utils import DataConnector


def main():
    inst_connect = DataConnector()
    aws_engine = inst_connect.read_db_creds('cred/db_creds.yaml')
    inst_connect.list_db_tables()
    
    # legacy_users = data_extractor.read_rds_table('legacy_users')
    # print(legacy_users.head())


if __name__ == "__main__":
    main()
