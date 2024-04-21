# evaluating sklearn model

# import libraries
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# function to evaluate the model
def evaluate_model(y_true, y_pred):
    ''' Evaluate the model
    Args:
        y_true (pandas.Series): Series containing the true target variable.
        y_pred (pandas.Series): Series containing the predicted target variable.
        
    Returns:
        dict: Dictionary containing the evaluation metrics.
        '''
    
    # calculate evaluation metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_pred)
    
    return {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1, 'auc': auc}