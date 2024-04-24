# script for hyperparameter tuning the decision tree model

# import libraries
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

# import user-defined functions
from data.load import load_data
from data.split import split_data
from data.preprocessing import one_hot_encode
from models.save import save_model

cur_dir = os.path.dirname(__file__) # current directory
root_dir = os.path.abspath(os.path.join(cur_dir, '..')) # root directory

# main function
def main():
    ''' Hyperparameter tuning for decision tree model
    '''
    
    # load data
    data = load_data(type='general', preprocessed=True)
    
    # one hot encode for categorical variables
    one_hot_cols = ['Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus']
    data = one_hot_encode(data, one_hot_cols, drop_first=False)

    # get X and y
    X = data.drop('Attrition', axis=1) # features
    y = data['Attrition'] # target variable

    # decision tree model
    model = DecisionTreeClassifier(random_state=0)

    # hyperparameters
    params = {'max_depth': [5, 10, 15, 20, 25, 30, 35, 40],
              'min_samples_split': [2, 5, 10, 15],
              'min_samples_leaf': [1, 2, 5, 10]}
    
    # grid search
    grid_search = GridSearchCV(model, param_grid=params, cv=7, scoring=['f1', 'roc_auc', 'accuracy'], refit='f1', n_jobs=-1)

    # fit the model
    grid_search.fit(X, y)

    # results
    results = pd.DataFrame(grid_search.cv_results_)

    # save results
    results.to_csv(root_dir + '/metrics/tree_grid_search_results.csv', index=False) # save the results

    # best hyperparameters
    print('Best hyperparameters:', grid_search.best_params_)
    print('Best f1 score:', grid_search.best_score_)

    # save the best model
    best_model = grid_search.best_estimator_
    save_model(best_model, root_dir + '/models/tree_grid_search/decision_tree_best.pkl')


# run the main function
if __name__ == '__main__':
    main()

