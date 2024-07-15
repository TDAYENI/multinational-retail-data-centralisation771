from data_extraction import Datadata_extractor
from database_utils import DataConnector
from data_cleaning import DataCleaning
import pandas as pd
# TODO LIST
# legacy_users_df = data_extractor.read_rds_table('legacy_users', aws_engine)

# * Cleaning users dataframe
# Cleans users data
legacy_users_clean = DataCleaning()

# replace nulls
cleaned_users = legacy_users_clean.replace_nulls(legacy_users_df)

# convert_dates to date time
date_columns = ['date_of_birth', 'join_date']
cleaned_users = legacy_users_clean.convert_dates(
    legacy_users_df, date_columns)

# remove non numeric characters
cleaned_users = legacy_users_clean.clean_numbers(
    legacy_users_df, column='phone_number')
# sets relevant data types
cleaned_users = legacy_users_clean.convert_data_types(legacy_users_df)
# drop null
cleaned_users = legacy_users_clean.drop_na(legacy_users_df)

# TODO un indent
pg_admin_connector.upload_to_db(
    pg_admin_engine, table_name='dim_users', data_frame=cleaned_users)


def main():
    # Initialise DataConnector to read database credentials and create an engine
    aws_connector = DataConnector()
    aws_engine = aws_connector.read_db_creds('cred/db_creds.yaml')

    # list all databases in connected DB
    aws_connector.list_db_tables()

    # extract data from 'orders_table
    data_extractor = Datadata_extractor()
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

    # Extracting data from a PDF
    pdf_extractor = Datadata_extractor()
    pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
    pdf_df = pdf_extractor .retrieve_pdf_df(link=pdf_link)

    #  PDF Cleaning
    pdf_cleaning_inst = DataCleaning()
    pdf_cleaned = pdf_cleaning_inst.replace_nulls(pdf_df)

    dates_list = ['date_payment_confirmed']
    pdf_cleaned = pdf_cleaning_inst.convert_dates(
        pdf_cleaned, date_columns=dates_list)

    pdf_cleaned = pdf_cleaning_inst.clean_numbers(
        pdf_cleaned, column='card_number')

    pdf_cleaned = pdf_cleaning_inst.drop_na(pdf_cleaned)

    # Upload PDF data to DB
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_card_details', data_frame=pdf_cleaned)

    # Retrieve number of stores from an API
    aws_header = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}
    store_num_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
    store_num_extractor = Datadata_extractor()
    # returns number of stores
    num_of_stores = store_num_extractor.list_number_of_stores(
        url=store_num_url, header=aws_header)

    # Retrieves data frame of store info
    stores_df = store_num_extractor.retrieve_stores_data(
        store_number=num_of_stores['number_stores'], header=aws_header)
    print(stores_df.head())

    # #Todo del products csv later
    # products_df = pd.read_csv('cred/stores_df.csv')

    # Cleans store data
    store_cleaner = DataCleaning()
    cleaned_store_data = store_cleaner.clean_store_data(stores_df)
    cleaned_store_data.to_csv('cred/cleaned_stores_df.csv')

    # upload stores data to postgres db
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_store_details',
        data_frame=cleaned_store_data)

    # Retrieve product data from S3
    aws_bucket = 'data-handling-public'
    s3_key = 'products.csv'
    local_path = 'cred/products.csv'
    s3_extractor = Datadata_extractor()
    products_df = s3_extractor.extract_from_s3(aws_bucket=aws_bucket,
                                               s3_key=s3_key, local_path=local_path)
    # Cleaning products data
    product_cleaner = DataCleaning()
    products_convert_kg = product_cleaner .convert_product_weights(
        data=products_df, weight_column='weight')
    cleaned_prod = product_cleaner .clean_products_data(
        data=products_convert_kg)
    print(cleaned_prod.head())
    # upload products table to db
    pg_admin_connector.upload_to_db(
        pg_admin_engine, table_name='dim_products',
        data_frame=cleaned_prod)


if __name__ == "__main__":
    main()
