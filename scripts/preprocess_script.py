# script for preprocessing the data

import pandas as pd
import os

# import the preprocessing functions
from data.load import load_data
from data.preprocessing import remove_columns, merge_data, impute_missing_values, \
    encode_target, label_encode, one_hot_encode, ordinal_encode

# root directory
cur_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.join(cur_dir, "..")


def main():
    ''' Main function for preprocessing the data
    '''

    # load the data
    general_data = load_data('general')
    manager_survey_data = load_data('manager_survey')
    employee_survey_data = load_data('employee_survey')
    in_time = load_data('in_time')
    out_time = load_data('out_time')

    # merge the data
    data = merge_data(general_data, manager_survey_data, employee_survey_data, 'EmployeeID')

    # remove unnecessary columns
    columns_to_remove = ['EmployeeCount', 'Over18', 'StandardHours']
    data = remove_columns(data, columns_to_remove)
    in_time = in_time.dropna(axis=1, how='all').reset_index(drop=True)
    out_time = out_time.dropna(axis=1, how='all').reset_index(drop=True)

    # convert all time columns to datetime
    in_time = in_time.apply(pd.to_datetime)
    out_time = out_time.apply(pd.to_datetime)

    # impute missing values
    cols_with_missing = data.columns[data.isnull().any()].tolist() # find all columns with missing values
    for col in cols_with_missing:
        data = impute_missing_values(data, col, method='mode') # impute missing values in the columns
    in_time = in_time.ffill(axis=1).bfill().dropna(axis=1)
    out_time = out_time.ffill(axis=1).bfill().dropna(axis=1)

    # find the time spent in the office
    time_spent = out_time - in_time
    mean_time = time_spent.mean(axis=1)
    mean_time = mean_time.apply(lambda x: x.total_seconds()) # change timedelta to seconds

    # encode target variable
    data = encode_target(data, 'Attrition')

    # label encode for ordinal variables
    ordinal_cols = ['BusinessTravel']
    order = [['Non-Travel', 'Travel_Rarely', 'Travel_Frequently']]
    data = ordinal_encode(data, ordinal_cols, order)

    # add the time spent column
    data['time_spent'] = mean_time

    # save the data
    data.to_csv(root_dir + '/data/preprocessed_data/general_data.csv', index=False)


# main function
if __name__ == '__main__':
    main()