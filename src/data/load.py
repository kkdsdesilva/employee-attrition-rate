# loding data from the data folder

import pandas as pd
import os
import sys

# path of the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# root directory
root_dir = os.path.join(current_dir, "../..")

# path to the data folder
data_dir = os.path.join(root_dir, "data")

# function to load data
def load_data(type='general', preprocessed=False):
    ''' Load data from the data folder
    Args:
        type (str): Type of data to load. Default is 'general'.
        Options are 'general', 'manager_survey', 'employee_survey', 'in_time', 'out_time'.

        preprocessed (bool): If True, load preprocessed data. Default is False.

    Returns:
        pandas.DataFrame: Dataframe containing the data.
    '''

    if preprocessed:
        if type == 'general':
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'general_data.csv'))
        
        elif type == 'in_time':
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'in_time.csv'), index_col=0)
        
        elif type == 'out_time':
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'out_time.csv'), index_col=0)
        
        else:
            print('Invalid type. Please choose from general, in_time, out_time for preprocessed data.')

    else:
        if type == 'general':
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'general_data.csv'))
        
        elif type == 'manager_survey':
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'manager_survey_data.csv'))
        
        elif type == 'employee_survey':
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'employee_survey_data.csv'))
        
        elif type == 'in_time':
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'in_time.csv'), index_col=0)
        
        elif type == 'out_time':
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'out_time.csv'), index_col=0)
