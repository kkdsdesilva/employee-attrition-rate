# decision tree model

# import libraries
from sklearn.tree import DecisionTreeClassifier

# function to train the model
def train_model(X, y, criterion='gini', max_depth=None, random_state=0, min_samples_split=2, min_samples_leaf=1):
    ''' Train a decision tree model
    Args:
        X (pandas.DataFrame): Dataframe containing the data.
        y (pandas.Series): Series containing the target variable.
        
    Returns:
        sklearn.tree.DecisionTreeClassifier: Trained decision tree model.
        '''
    
    # initialize the model
    model = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth, random_state=random_state)
    
    # fit the model
    model.fit(X, y)
    
    return model