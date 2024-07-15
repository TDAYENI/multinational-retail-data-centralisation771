

import requests
from sqlalchemy import inspect
from sqlalchemy import text
import pandas as pd
import tabula
import boto3
import requests

# Todo The methods contained will be fit to extract data from a particular data source,
# Todo these sources will include CSV files, an API and an S3 bucket


class DataExtractor:

    # class to read the data from the RDS database

    def read_rds_table(self, table_name, engine):
        db_df = pd.read_sql_table(table_name, engine)
        return db_df

    # Todo extract the database table to a pandas DataFrame
    #  TODO ke in an instance of your DatabaseConnector class and
    # TODO the table name as an argument and return a pandas DataFrame.
    def retrieve_pdf_data(self, link):
        pdf_df = tabula.read_pdf(link, pages='all')
        pandas_pdf = pd.concat(pdf_df, ignore_index=True)
        return pandas_pdf

    def list_number_of_stores(self, url, header):

        try:
            response = requests.get(url, headers=header)
            # This will raise an HTTPError for bad responses (4xx and 5xx)
            response.raise_for_status()

            # Process the response if no exceptions were raised
            data = response.json()  # Assuming the response is in JSON format
            print(data)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        except ValueError as json_err:
            print(f"JSON decoding failed: {json_err}")
        return data

    def retrieve_stores_data(self, store_number, header):
        store_data = []

        for store_number_index in range(0, store_number):

            try:
                response = requests.get(
                    f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number_index}', headers=header)
                # This will raise an HTTPError for bad responses (4xx and 5xx)
                response.raise_for_status()

                # Process the response if no exceptions were raised
                data = response.json()  # Assuming the response is in JSON format
                store_data.append(data)

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err}")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"An error occurred: {req_err}")
            except ValueError as json_err:
                print(f"JSON decoding failed: {json_err}")

        return pd.DataFrame(store_data)

    def extract_from_s3(self, aws_bucket, s3_key, local_path):
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=aws_bucket, Key=s3_key)

        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

        if status == 200:
            print(f"Successful S3 get_object response. Status - {status}")
            products_df = pd.read_csv(response.get("Body"))
            return products_df
        else:
            print(f"Unsuccessful S3 get_object response. Status - {status}")
        



