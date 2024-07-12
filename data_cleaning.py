import numpy as np
import re
import pandas as pd


class DataCleaning:
    # Todo ook out for NULL values, errors with dates, incorrectly
    # Todo typed values and rows filled with the wrong information
    def replace_nulls(self, data, null_value='NULL', replacement=np.nan):
        return data.replace(null_value, replacement)

    def convert_dates(self, data, date_columns_list, date_format='%Y-%m-%d'):
        for column in date_columns_list:
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

    def column_to_numeric(self, data, numeric_column):
        """Convert panda vlaues to best data types"""
        data[numeric_column] = pd.to_numeric(
            data[numeric_column], downcast='integer', errors='coerce')
        return data

    def drop_column(self, data, dropped_column):
        dropped_data = data.drop(dropped_column, axis=1)
        return dropped_data

    def drop_na(self, data):
        return data.dropna()

    def clean_store_data(self, data):
        cleaned_dates = self.convert_dates(data, date_columns_list=['opening_date'])
        # cleaned_numeric = self.column_to_numeric(
        #     data=cleaned_dates, numeric_column='staff_numbers')
        return cleaned_dates
