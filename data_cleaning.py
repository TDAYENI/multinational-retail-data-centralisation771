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
        
        for column in strings_column_list:
            cleaned_user[column] = cleaned_user[column].astype('string')

        cleaned_user = cleaned_user.dropna()

        return cleaned_user
