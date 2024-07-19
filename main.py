from data_extraction import DataExtractor
from database_utils import DataConnector
from data_cleaning import DataCleaning
import pandas as pd
import os
from dotenv import load_dotenv

 
def main():
    # Initialise DataConnector to read database credentials and create an engine
    aws_connector = DataConnector()
    aws_engine = aws_connector.read_db_creds('cred/db_creds.yaml')

    # list all databases in connected DB
    aws_connector.list_db_tables()

    # extract data from 'orders_table
    data_extractor = DataExtractor()
    orders_table_df = data_extractor.read_rds_table('orders_table', aws_engine)

    # Cleans orders table
    orders_table_clean = DataCleaning()
    cleaned_orders_table = orders_table_clean.clean_orders_data(
        data=orders_table_df)

    # Intialise pg admin  db conection and read credential
    pg_admin_connector = DataConnector()
    pg_admin_engine = pg_admin_connector.read_db_creds(
        'cred/pg_admin_creds.yaml')

    # Upload the cleaned orders table to the db
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='orders_table',
        data_frame=cleaned_orders_table)

    # TODO LIST
    data_extractor = DataExtractor()
    legacy_users_df = data_extractor.read_rds_table('legacy_users', aws_engine)

    # * Cleaning users dataframe
    # Cleans users data
    user_dates_cols = ['date_of_birth', 'join_date']
    user_num_column = 'phone_number'
    legacy_users_clean = DataCleaning()
    cleaned_users = legacy_users_clean.clean_users(
        data=legacy_users_df, user_dates_cols=user_dates_cols, user_num_column=user_num_column)
    # uploading cleaned users data to db
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_users', data_frame=cleaned_users)

    #* Extracting data from a PDF
    pdf_extractor = DataExtractor()
    pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
    pdf_df = pdf_extractor .retrieve_pdf_df(link=pdf_link)

    #  PDF Cleaning
    dates_list = ['date_payment_confirmed']
    card_column = 'card_number'

    pdf_cleaning_inst = DataCleaning()
    pdf_cleaned = pdf_cleaning_inst.clean_pdf(data=pdf_df, dates_list=dates_list, card_num_column=card_column)

    # Upload PDF data to DB
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_card_details', data_frame=pdf_cleaned)

 
    #* Retrieve number of stores from an API
    load_dotenv()
    aws_api_key = os.getenv('AWS_API_KEY')

    aws_header = {"x-api-key": aws_api_key}

    store_num_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
    store_num_extractor = DataExtractor()
    # returns number of stores
    num_of_stores = store_num_extractor.list_number_of_stores(
        url=store_num_url, header=aws_header)

    # Retrieves data frame of store info
    stores_df = store_num_extractor.retrieve_stores_data(
        store_number=num_of_stores['number_stores'], header=aws_header)
    

    #* Cleans store data
    store_cleaner = DataCleaning()
    cleaned_store_data = store_cleaner.clean_store_data(stores_df)

    # upload stores data to postgres db
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_store_details',
        data_frame=cleaned_store_data)

    # * Retrieve product data from S3
    aws_bucket = 'data-handling-public'
    s3_key = 'products.csv'
    local_path = 'cred/products.csv'
    s3_extractor = DataExtractor()
    products_df = s3_extractor.extract_from_s3(aws_bucket=aws_bucket,
                                               s3_key=s3_key, local_path=local_path)
    # * Cleaning products data
    weight_column = 'weight'
    prod_dates_list = ['date_added']
    product_cleaner = DataCleaning()
    prod_weight_conv = product_cleaner.convert_product_weights(data=products_df, weight_column=weight_column
       )
    cleaned_prod = product_cleaner .clean_products_data(
        data=prod_weight_conv, prod_dates_list=prod_dates_list)

    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_products',
        data_frame=cleaned_prod)


if __name__ == "__main__":
    main()
