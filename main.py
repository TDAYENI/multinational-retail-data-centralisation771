from data_extraction import DataExtractor
from database_utils import DataConnector
from data_cleaning import DataCleaning
import pandas as pd


def main():
    # #* Reading DB
    # # reads database creds and returns engine
    # inst_connect = DataConnector()
    # aws_engine = inst_connect.read_db_creds('cred/db_creds.yaml')

    # inst_connect.list_db_tables()
    # # returns data frame of leagcy users
    # extractor = DataExtractor()
    # legacy_users_df = extractor.read_rds_table('legacy_users', aws_engine)
    # # * Cleaning users dataframe
    # # Cleans users data
    # legacy_users_clean = DataCleaning()

    # # replace nulls
    # cleaned_users = legacy_users_clean.replace_nulls(legacy_users_df)

    # # convert_dates to date time
    # date_columns = ['date_of_birth', 'join_date']
    # cleaned_users = legacy_users_clean.convert_dates(
    #     legacy_users_df, date_columns)

    # # remove non numeric characters
    # cleaned_users = legacy_users_clean.clean_numbers(
    #     legacy_users_df, column='phone_number')
    # # sets relevant data types
    # cleaned_users = legacy_users_clean.convert_data_types(legacy_users_df)
    # # drop null
    # cleaned_users = legacy_users_clean.drop_na(legacy_users_df)

    # #* Upload Users Data to DB
    #  # retrieve database cred to upload to datasales
    # pg_admin_inst = DataConnector()
    # pg_admin_engine = pg_admin_inst.read_db_creds('cred/pg_admin_creds.yaml')
    # print(pg_admin_engine)
    # pg_admin_inst.upload_to_db(pg_admin_engine, table_name='dim_users',data_frame=cleaned_users)

    # # TODO from up here ctl /
    # # * PDF Section
    # # Retrieving and creating pdf as pd data frame
    # pdf_inst = DataExtractor()
    # pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
    # pdf_data = pdf_inst.retrieve_pdf_data(link=pdf_link)
    # breakpoint()
    # # * PDF Cleaning
    # pdf_cleaning_inst = DataCleaning()

    # pdf_cleaned = pdf_cleaning_inst.replace_nulls(pdf_data)

    # dates_list = ['date_payment_confirmed']
    # pdf_cleaned = pdf_cleaning_inst.convert_dates(
    #     pdf_cleaned, date_columns=dates_list)
    # # TODO change date of confirmed ID
    # pdf_cleaned = pdf_cleaning_inst.clean_numbers(
    #     pdf_cleaned, column='card_number')

    # pdf_cleaned = pdf_cleaning_inst.drop_na(pdf_cleaned)

    # # * Upload PDF Data to DB
    # # retrieve database cred to upload to datasales

    # pg_admin_inst.upload_to_db(
    #     pg_admin_engine, table_name='dim_card_details', data_frame=pdf_cleaned)


    # # * Retrieve Product data
    # aws_header = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
    # store_num_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
    # store_num_inst = DataExtractor()
    # # returns a
    # num_of_stores = store_num_inst.list_number_of_stores(
    #     url=store_num_url, header=aws_header)
    
    # # Returns data frame of all stores info
    # stores_df = store_num_inst.retrieve_stores_data(
    #     store_number=num_of_stores['number_stores'], header=aws_header)
    # print(stores_df.head())

    # #Todo del products csv later
    # products_df = pd.read_csv('cred/stores_df.csv')

    
    # store_inst = DataCleaning()

    # cleaned_store_data = store_inst.clean_store_data(products_df)
    # cleaned_store_data.to_csv('cred/cleaned_stores_df.csv')

    # #* repeat code del upload store data to pg db
    # pg_admin_inst = DataConnector()
    # pg_admin_engine = pg_admin_inst.read_db_creds('cred/pg_admin_creds.yaml')
    # print(pg_admin_engine)
    # pg_admin_inst.upload_to_db(
    #     pg_admin_engine, table_name='dim_store_details',
    #     data_frame=cleaned_store_data)
    # TODO from here up
    aws_bucket = 'data-handling-public'
    s3_key = 'products.csv'
    local_path = 'cred/products.csv'
    s3_inst= DataExtractor()

    products_df=s3_inst.extract_from_s3(aws_bucket=aws_bucket,
                            s3_key=s3_key, local_path=local_path)
    
    products_inst = DataCleaning()
    products_convert_kg = products_inst.convert_product_weights(
        data=products_df, weight_column='weight')
    cleaned_prod = products_inst.clean_products_data(data=products_convert_kg)
    print(cleaned_prod.head())

    cleaned_prod.to_csv('cred/cleaned_prod.csv')

    pg_admin_inst = DataConnector()
    pg_admin_engine = pg_admin_inst.read_db_creds('cred/pg_admin_creds.yaml')
    print(pg_admin_engine)
    pg_admin_inst.upload_to_db(
        pg_admin_engine, table_name='dim_products',
        data_frame=cleaned_prod)
if __name__ == "__main__":
    main()

   # cleaned_users_df = legacy_users_clean.clean_user_data(legacy_users_df.info)

    # #
    # pg_admin_inst.upload_to_db(
    #     pg_admin_engine, 'dim_users', cleaned_users_df)

    # legacy_users = data_extractor.read_rds_table('legacy_users')
    # print(legacy_users.head())
