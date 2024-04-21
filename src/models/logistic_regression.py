# logistic regression model

# import libraries
from sklearn.linear_model import LogisticRegression

# function to train the model
def train_model(X, y, C=1.0, max_iter=1000, random_state=0):
    ''' Train a logistic regression model
    Args:
        X (pandas.DataFrame): Dataframe containing the data.
        y (pandas.Series): Series containing the target variable.
        
    Returns:
        sklearn.linear_model.LogisticRegression: Trained logistic regression model.
        '''
    
    # initialize the model
    model = LogisticRegression(C=C, max_iter=max_iter, random_state=random_state)
    
    # fit the model
    model.fit(X, y)
    
    return model