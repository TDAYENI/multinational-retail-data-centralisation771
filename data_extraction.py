
import requests
from sqlalchemy import inspect
from sqlalchemy import text
import pandas as pd
import tabula
import boto3
import requests



class DataExtractor:
    """_summary_
 A class used to extract data from various sources including RDS databases, PDFs, APIs, and S3 buckets.

    Methods
    -------
    read_rds_table(table_name, engine)
        Reads a table from an RDS database into a DataFrame.

    retrieve_pdf_data(link)
        Extracts data from a PDF file and returns it as a DataFrame.

    retrieve_json(url, header)
        retrieves data from a JSON API and returns it as a DataFrame.

    retrieve_number_of_stores(url, headers)
        gets the number of stores from an API.

    retrieve_store_data(store_number, header)
        Retrieves detailed store data from an API.

    extract_from_s3(aws_bucket, s3_key, local_path)
        Downloads  CSV  from an S3 bucket returning a DataFrame.
    """

    def read_rds_table(self, table_name, engine):
        """_summary_
         Extracts data from a PDF file and returns it as a DataFrame
        Parameters
        ----------
        table_name : str
            The name of the table to read
        engine : Engine
             SQLAlchemy engine instance

        Returns
        -------
        DataFrame: The table data as a pandas DataFrame.
    
        """
        db_df = pd.read_sql_table(table_name, engine)
        return db_df


    def retrieve_pdf_df(self, link):
        """
        Gets the number of stores from an API

        Parameters
        ----------
        link :(str): URL or path to the PDF file

        Returns
        -------
       DataFrame: The PDF data as a pandas DataFrame
        """

        pdf_df = tabula.read_pdf(link, pages='all',stream= False)
        pandas_pdf = pd.concat(pdf_df, ignore_index=True)
        return pandas_pdf

    def retrieve_json(self, url, header):
        """
        Gets the number of stores from an API

        Parameters
        ----------
        url :  (str): The API endpoint URL.
        header :(dict): The headers to include in the API request.

        Returns
        -------
         int: The number of stores.
        """

        try:
            response = requests.get(url, headers=header)
            # This will raise an HTTPError for bad responses (4xx and 5xx)
            response.raise_for_status()

            # Process the response if no exceptions were raised
            data = response.json()  # Assuming the response is in JSON format
            
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
        """
        Retrieves detailed store data from an API.

        Parameters
        ----------
        store_number : (int) The number of stores to retrieve data for.
        header : (dict)The headers to include in the API request.

        Returns
        -------
        pandas DataFrame The detailed store data as a pandas DataFrame.
        """
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
