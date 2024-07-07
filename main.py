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

    # replace nulls
    cleaned_users = legacy_users_clean.replace_nulls(legacy_users_df)

    # convert_dates
    date_columns = ['date_of_birth', 'join_date']
    cleaned_users = legacy_users_clean.convert_dates(
        legacy_users_df, date_columns)
    # clean phone data
    cleaned_users = legacy_users_clean.clean_phone_numbers(
        legacy_users_df, phone_column='phone_number')
    # convert_data_types
    cleaned_users = legacy_users_clean.convert_data_types(legacy_users_df)
    # drop null
    cleaned_users = legacy_users_clean.drop_na(legacy_users_df)
    print(cleaned_users.info())

    # cleaned_users_df = legacy_users_clean.clean_user_data(legacy_users_df.info)

    # # retrieve database cred to upload to datasales
    # pg_admin_inst = DataConnector()
    # pg_admin_engine = pg_admin_inst.read_db_creds('cred/pg_admin_creds.yaml')
    # print(pg_admin_engine)

    # #
    # pg_admin_inst.upload_to_db(
    #     pg_admin_engine, 'dim_users', cleaned_users_df)

    # legacy_users = data_extractor.read_rds_table('legacy_users')
    # print(legacy_users.head())
if __name__ == "__main__":
    main()
