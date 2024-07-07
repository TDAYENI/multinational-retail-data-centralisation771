from data_extraction import DataExtractor
from database_utils import DataConnector
from data_cleaning import DataCleaning


def main():
    inst_connect = DataConnector()
    # reads database creds and returns engine
    aws_engine = inst_connect.read_db_creds('cred/db_creds.yaml')
    # aws_engine = inst_connect.read_db_creds('cred/pg_admin_creds.yaml')
    inst_connect.list_db_tables()

    extractor = DataExtractor()
    # returns data frame of leagcy users
    legacy_users_df = extractor.read_rds_table('legacy_users', aws_engine)
    # returns cleaned data to be uploaded to
    legacy_users_clean = DataCleaning()
    cleaned_users_df = legacy_users_clean.clean_user_data(legacy_users_df)

    # retrieve database cred to upload to datasales
    pg_admin_inst = DataConnector()
    pg_admin_engine = pg_admin_inst.read_db_creds('cred/pg_admin_creds.yaml')
    print(pg_admin_engine)

    #
    pg_admin_inst.upload_to_db(
        pg_admin_engine, 'dim_users', cleaned_users_df)

    # legacy_users = data_extractor.read_rds_table('legacy_users')
    # print(legacy_users.head())
if __name__ == "__main__":
    main()
