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
    #returns data frame of leagcy users
    legacy_users_df = extractor.read_rds_table('legacy_users', aws_engine)

    legacy_users_clean = DataCleaning()
    cleaned_users_df = legacy_users_clean.clean_user_data(legacy_users_df)
    print(cleaned_users_df)



    
    # legacy_users = data_extractor.read_rds_table('legacy_users')
    # print(legacy_users.head())


if __name__ == "__main__":
    main()
