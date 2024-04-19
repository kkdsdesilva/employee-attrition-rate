# preprocessing functions

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler, MinMaxScaler

# remove unnecessary columns
def remove_columns(data, columns):
    ''' Remove unnecessary columns from the data
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        columns (list): List of columns to remove from the data.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data after removing the columns.
        '''
    
    return data.drop(columns=columns)


# merge three dataframes
def merge_data(data1, data2, data3, on, how='inner'):
    ''' Merge three dataframes on a common column
    Args:
        data1 (pandas.DataFrame): First dataframe to merge.
        data2 (pandas.DataFrame): Second dataframe to merge.
        data3 (pandas.DataFrame): Third dataframe to merge.
        on (str): Column name to merge on.
        how (str): Type of merge. Default is 'inner'.
        
    Returns:
        pandas.DataFrame: Dataframe containing the merged data.
        '''
    return pd.merge(pd.merge(data1, data2, on=on, how=how), data3, on=on, how=how)


# impuation of missing values
def impute_missing_values(data, col, method='mean'):
    ''' Impute missing values in the data
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        col (str): Column name to impute missing values.
        method (str): Imputation method. Default is 'mean'.
        Options are 'mean', 'median', 'mode'.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data after imputing missing values.
        '''
    
    if method == 'mean':
        data[col] = data[col].fillna(data[col].mean())

    elif method == 'median':
        data[col] = data[col].fillna(data[col].median())

    elif method == 'mode':
        data[col] = data[col].fillna(data[col].mode()[0])

    return data


# encoding target variable
def encode_target(data, target):
    ''' Encode the target variable
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        target (str): Target variable to encode.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data with encoded target variable.
        '''
    
    data[target] = data[target].map({'Yes': 1, 'No': 0})
    return data


# label encoding categorical variables
def label_encode(data, cols):
    ''' Label encode the categorical variables
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        cols (list): List of columns to label encode.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data with label encoded columns.
        '''
    
    le = LabelEncoder()
    for col in cols:
        data[col] = le.fit_transform(data[col])
    
    return data

# one hot encoding categorical variables
def one_hot_encode(data, cols, drop_first=True):
    ''' One hot encode the categorical variables
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        cols (list): List of columns to one hot encode.
        drop_first (bool): Whether to drop the first level. Default is True.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data with one hot encoded columns.
        '''
    
    data = pd.get_dummies(data, columns=cols, drop_first=drop_first)

    return data

# ordinal encoding categorical variables
def ordinal_encode(data, cols, orderings='auto'):
    ''' Ordinal encode the categorical variables
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        cols (list): List of columns to ordinal encode.
        orderings (list): List of orderings for each column.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data with ordinal encoded columns.
        '''
    
    oe = OrdinalEncoder(categories=orderings)

    data[cols] = oe.fit_transform(data[cols])
    
    return data

# scaling numerical variables
def scale_data(data, cols, scaler='standard'):
    ''' Scale the numerical variables
    Args:
        data (pandas.DataFrame): Dataframe containing the data.
        cols (list): List of columns to scale.
        scaler (str): Type of scaler. Default is 'standard'.
        Options are 'standard', 'minmax'.
        
    Returns:
        pandas.DataFrame: Dataframe containing the data with scaled columns.
        '''
    
    if scaler == 'standard':
        sc = StandardScaler()
    elif scaler == 'minmax':
        sc = MinMaxScaler()
    
    data[cols] = sc.fit_transform(data[cols])
    
    return data



