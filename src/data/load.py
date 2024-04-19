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
    if type == 'general':
        if preprocessed:
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'general_data.csv'))
        else:
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'general_data.csv'))
        
    elif type == 'survey':
        if preprocessed:
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'manager_survey_data.csv'))
        else:
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'manager_survey_data.csv'))
        
    elif type == 'employee':
        if preprocessed:
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'employee_survey_data.csv'))
        else:
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'employee_survey_data.csv'))
        
    elif type == 'in_time':
        if preprocessed:
            return pd.read_csv(os.path.join(data_dir, 'preprocessed_data', 'in_time_data.csv'), index_col=0)
        else:
            return pd.read_csv(os.path.join(data_dir, 'raw_data', 'in_time_data.csv'), index_col=0)