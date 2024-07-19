import numpy as np
import re
import pandas as pd


class DataCleaning:
    # Todo ook out for NULL values, errors with dates, incorrectly
    # Todo typed values and rows filled with the wrong information
    def replace_nulls(self, data, null_value='NULL', replacement=np.nan):
        return data.replace(null_value, replacement)

    def convert_dates(self, data, date_columns_list, date_format='mixed'):
        for column in date_columns_list:
            data[column] = pd.to_datetime(
                data[column], format=date_format, errors='coerce')
        return data

    def clean_numbers(self, data, column):
        """Removes non numeric characters using regex"""
        data[column] = data[column].astype('string')
        data[column] = data[column].apply(
            lambda x: re.sub(r'\D', '', x) if pd.notnull(x) else x)
        return data.copy()

    def clean_store_code(self, data, column):
        """Replaces item with """
        data[column] = data[column].apply(
            lambda x: x if '-' in str(x) else np.nan)
        return data.copy()

    def convert_data_types(self, data):
        """Convert panda vlaues to best data types"""
        return data.convert_dtypes()

    def column_to_numeric(self, data, numeric_column):
        """Convert pandas values to numeric type"""
        data.loc[:, numeric_column] = pd.to_numeric(
            data[numeric_column], errors='coerce')
        return data

    def column_as_type(self, data, as_type_column, type):
        """Convert pandas column to specified data type"""
        data.loc[:, as_type_column] = data[as_type_column].astype(
            type)  # Use .loc to avoid SettingWithCopyWarning
        return data

    def drop_column(self, data, dropped_column):
        return data.drop(dropped_column, axis=1)

    def drop_na(self, data):
        return data.dropna()

    def thresh_drop_na(self, data, threshold=1):
        # drop rows with two or more missing values
        num_columns = data.shape[1]
        data.dropna(thresh=num_columns - threshold, inplace=True)
        return data

    def strip_string(self, data, string_column, remove_char):
        data[string_column] = data[string_column].str.replace(remove_char, '')
        return data

    def clean_store_data(self, data):
        cleaned_data = (
            data.pipe(self.clean_numbers, column='store_code')
            .pipe(self.convert_dates, date_columns_list=['opening_date'])
            .pipe(self.clean_numbers, column='staff_numbers')
            .pipe(self.column_to_numeric, numeric_column='latitude')
            .pipe(self.column_to_numeric, numeric_column='longitude')
            .pipe(self.strip_string, string_column='continent', remove_char='ee')
            .pipe(self.replace_nulls, null_value=['NULL', ''])
            .pipe(self.thresh_drop_na)
            .pipe(self.drop_column, dropped_column='lat')
            .pipe(self.replace_nulls, null_value='N/A', replacement='0')
        )

        return cleaned_data

    def clean_pdf(self, data, dates_list, card_num_column):
        cleaned_data = (
            data.pipe(self.replace_nulls)
            .pipe(self.convert_dates, date_columns_list=dates_list)
            .pipe(self.clean_numbers, column=card_num_column)
            .pipe(self.drop_na)
        )

        return cleaned_data

    def convert_product_weights(self, data, weight_column):
        def convert_weights(weights):
            # Handle multiple units (e.g., "8 x 85g")
            multiple_match = re.match(
                r'(\d+)\s*x\s*(\d+\.?\d*)(\w+)', weights)
            if multiple_match:
                count = int(multiple_match.group(1))
                value = float(multiple_match.group(2))
                unit = multiple_match.group(3)
                weight_value = count * value
            else:
                # Extract value and unit
                match = re.match(r'(\d+\.?\d*)(\w+)', weights)
                if not match:
                    return None
                weight_value = float(match.group(1))
                unit = match.group(2)

            # Conversion factors
            if unit == 'kg':
                return weight_value
            elif unit == 'g':
                return weight_value * 0.001
            elif unit == 'ml':
                return weight_value * 0.001  # Assuming 1:1 ratio for ml to g
            elif unit == 'oz':
                return weight_value * 0.0283495
            else:
                return None  # Unknown unit
        data[weight_column] = data[weight_column].astype(
            str).apply(convert_weights)
        return data

    def clean_products_data(self, data, prod_dates_list):
        cleaned_data = (
            data.pipe(self.convert_dates, date_columns_list=prod_dates_list)
            .pipe(self.replace_nulls)
            .pipe(self.drop_na))
        return cleaned_data

    def clean_orders_data(self, data):
        cleaned_data = (
            data.pipe(self.drop_column, dropped_column='first_name')
            .pipe(self.drop_column, dropped_column='last_name')
            .pipe(self.drop_column, dropped_column='1')
        )
        return cleaned_data

    def clean_users(self, data, user_dates_cols, user_num_column):
        cleaned_data = (
            data.pipe(self.convert_dates, date_columns_list=user_dates_cols)
            .pipe(self.clean_numbers, column=user_num_column)
            .pipe(self.convert_data_types)
            .pipe(self.replace_nulls)
            .pipe(self.drop_na)
        )

        return cleaned_data

    def clean_dates_details(self, data):
        cleaned_data = (
            data.pipe(self.column_to_numeric, numeric_column='month')
            .pipe(self.drop_na)
            .pipe(self.column_as_type, as_type_column='month', type='int64')

        )
        return cleaned_data
