# split data into train and test data

import pandas as pd
from sklearn.model_selection import train_test_split

# function to split data
def split_data(data, target, test_size=0.2, random_state=0, stratify=True):
    ''' Split data into train and validation
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        target (str): Target variable.
        test_size (float): Proportion of data to include in the validation set. Default is 0.2.
        random_state (int): Random state. Default is 0.
        
    Returns:
        pandas.DataFrame: Dataframe containing the train data.
        pandas.DataFrame: Dataframe containing the validation data.
        pandas.Series: Series containing the target variable for train data.
        pandas.Series: Series containing the target variable for validation data.
        '''
    
    # split data
    train, test = train_test_split(data, test_size=test_size, random_state=random_state, stratify=data[target] if stratify else None)
    
    # split target variable
    X_train, y_train = train.drop(columns=[target]), train[target]
    X_test, y_test = test.drop(columns=[target]), test[target]
    
    # return split data
    return X_train, X_test, y_train, y_test
