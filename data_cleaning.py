import numpy as np
import re
import pandas as pd


class DataCleaning:
    # Todo ook out for NULL values, errors with dates, incorrectly
    # Todo typed values and rows filled with the wrong information
    def clean_user_data(self, user_data):
        cleaned_user = user_data.copy()
        date_columns = ['date_of_birth', 'join_date']
        
        cleaned_user.replace('NULL', np.nan)
        for dates in date_columns:
            cleaned_user[dates] = pd.to_datetime(cleaned_user[dates],format='%Y-%m-%d', errors='coerce')

        return print('cleaned data',cleaned_user)
        
