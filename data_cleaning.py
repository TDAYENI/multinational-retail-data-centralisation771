import numpy as np
import re
import pandas as pd


class DataCleaning:
    # Todo ook out for NULL values, errors with dates, incorrectly
    # Todo typed values and rows filled with the wrong information
    def replace_nulls(self, data, null_value='NULL', replacement=np.nan):
        return data.replace(null_value, replacement)

    def convert_dates(self, data, date_columns, date_format='%Y-%m-%d'):
        for column in date_columns:
            data[column] = pd.to_datetime(
                data[column], format=date_format, errors='coerce')
        return data.copy()

    def clean_numbers(self, data, column):
        """Removes non numeric characters using regex"""
        data[column] = data[column].astype('string')
        data[column] = data[column].apply(
            lambda x: re.sub(r'\D', '', x) if pd.notnull(x) else x)
        return data.copy()

    def convert_data_types(self, data):
        """Convert panda vlaues to best data types"""
        return data.convert_dtypes()

    def drop_na(self, data):
        return data.dropna()
