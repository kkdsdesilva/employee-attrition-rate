# cross-validation

# import libraries
from sklearn.model_selection import cross_validate

# function for cross-validation
def cv(X, y, model, cv=5, scoring=['accuracy', 'precision', 'recall', 'f1', 'roc_auc']):
    ''' Perform cross-validation
    Args:
        X (pandas.DataFrame): Dataframe containing the data.
        y (pandas.Series): Series containing the target variable.
        model (sklearn estimator): Model to be cross-validated.
        cv (int): Number of folds. Default is 5.
        scoring (list): List of evaluation metrics. Default is ['accuracy', 'precision', 'recall', 'f1', 'roc_auc'].
        
    Returns:
        dict: Dictionary containing the evaluation metrics for each fold.
        '''
    
    # perform cross-validation
    results = cross_validate(model, X, y, cv=cv, scoring=scoring)
    
    return results