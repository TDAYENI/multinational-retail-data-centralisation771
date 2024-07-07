import numpy as np
import re
import pandas as pd


class DataCleaning:
    # Todo ook out for NULL values, errors with dates, incorrectly
    # Todo typed values and rows filled with the wrong information
    def clean_user_data(self, user_data):
        cleaned_user = user_data.copy()
        date_columns = ['date_of_birth', 'join_date']
        strings_column_list = ['first_name', 'last_name', 'date_of_birth',
                               'company', 'email_address', 'address', 'phone_number', 'user_uuid']

        cleaned_user.replace('NULL', np.nan)
        for dates in date_columns:
            cleaned_user[dates] = pd.to_datetime(
                cleaned_user[dates], format='%Y-%m-%d', errors='coerce')
        # regex expression cleans user info
        cleaned_user['phone_number'] = cleaned_user['phone_number'].apply(
            lambda x: re.sub(r'\D', '', x) if pd.notnull(x) else x)
        # correct the data types
        cleaned_user = cleaned_user.convert_dtypes()
        cleaned_user = cleaned_user.dropna()

    def replace_nulls(self, data, null_value='NULL', replacement=np.nan):
        return data.replace(null_value, replacement)

    def convert_dates(self, data, date_columns, date_format='%Y-%m-%d'):
        for column in date_columns:
            data[column] = pd.to_datetime(
                data[column], format=date_format, errors='coerce')
        return data

    def clean_phone_numbers(self, data, phone_column):
        """Removes non numeric characters using regex"""
        data[phone_column] = data[phone_column].apply(
            lambda x: re.sub(r'\D', '', x) if pd.notnull(x) else x)
        return data

    def convert_data_types(self, data):
        """Convert panda vlaues to best data types"""
        return data.convert_dtypes()

    def drop_na(self, data):
        return data.dropna()
