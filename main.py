from data_extraction import DataExtractor
from database_utils import DataConnector


def main():
    inst_connect = DataConnector()
    aws_engine = inst_connect.read_db_creds('cred/db_creds.yaml')
    # aws_engine = inst_connect.read_db_creds('cred/pg_admin_creds.yaml')
    inst_connect.list_db_tables()
    extractor = DataExtractor()
    legacy_users = extractor.read_rds_table('legacy_users', aws_engine)
    print(legacy_users.head())
    # legacy_users = data_extractor.read_rds_table('legacy_users')
    # print(legacy_users.head())


if __name__ == "__main__":
    main()
