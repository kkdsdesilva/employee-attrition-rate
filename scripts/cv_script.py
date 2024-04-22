# script for cross-validation

# import libraries
import pandas as pd
import os

# import user-defined functions
from data.load import load_data
from data.split import split_data
from data.preprocessing import one_hot_encode
from models.decision_tree import train_model
from models.evaluation import evaluate_model
from models.cross_validation import cv 
from models.save import save_model

# root directory
cur_dir = os.path.dirname(__file__) # current directory
root_dir = os.path.abspath(os.path.join(cur_dir, '..')) # root directory

# main function
def main():
    ''' Perform cross-validation on decision tree model
    '''
    
    # load data
    data = load_data(type='general', preprocessed=True)

    # one hot encode for categorical variables
    one_hot_cols = ['Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus']
    data = one_hot_encode(data, one_hot_cols, drop_first=False)

    # split data
    X_train, X_test, y_train, y_test = split_data(data, target='Attrition', test_size=0.1)

    # import decision tree model
    from sklearn.tree import DecisionTreeClassifier
    model = DecisionTreeClassifier(random_state=0)

    # perform cross-validation
    cv_results = cv(X_train, y_train, model, cv=7)

    # print cross-validation results
    print(pd.DataFrame(cv_results))

    # save cross-validation results
    cv_results_df = pd.DataFrame(cv_results)
    cv_results_df.to_csv(root_dir+'/metrics/cv_results.csv', index=False)

# run the main function
if __name__ == '__main__':
    main()

