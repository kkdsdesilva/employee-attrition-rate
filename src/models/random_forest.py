# random forest model

# import libraries
from sklearn.ensemble import RandomForestClassifier

# function to train the model
def train_model(X, y, criterion='gini', n_estimators=100, max_depth=None, min_samples_split=2, min_samples_leaf=1, random_state=0):
    ''' Train a random forest model
    Args:
        X (pandas.DataFrame): Dataframe containing the data.
        y (pandas.Series): Series containing the target variable.
        
    Returns:
        sklearn.ensemble.RandomForestClassifier: Trained random forest model.
        '''
    
    # initialize the model
    model = RandomForestClassifier(criterion=criterion, n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    
    # fit the model
    model.fit(X, y)
    
    return model