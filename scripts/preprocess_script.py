# script for preprocessing the data

import pandas as pd
import os

# import the preprocessing functions
from data.load import load_data
from data.preprocess import remove_columns, merge_data, impute_missing_values, \
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
    in_time_data = load_data('in_time')
    out_time_data = load_data('out_time')


    # merge the data
    data = merge_data(general_data, manager_survey_data, employee_survey_data, 'EmployeeID')


    # remove unnecessary columns
    columns_to_remove = ['EmployeeCount', 'Over18', 'StandardHours']
    data = remove_columns(data, columns_to_remove)


    # impute missing values
    cols_with_missing = data.columns[data.isnull().any()].tolist() # find all columns with missing values

    for col in cols_with_missing:
        data = impute_missing_values(data, col, method='mode') # impute missing values in the columns


    # encode target variable
    data = encode_target(data, 'Attrition')


    # label encode for ordinal variables
    ordinal_cols = ['BusinessTravel']
    order = [['Non-Travel', 'Travel_Rarely', 'Travel_Frequently']]
    data = ordinal_encode(data, ordinal_cols, order)

    # save the data
    data.to_csv(root_dir + '/data/preprocessed_data/general_data.csv', index=False)


    # one hot encode for categorical variables
    #one_hot_cols = ['Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus']
    #data = one_hot_encode(data, one_hot_cols)

# main function
if __name__ == '__main__':
    main()