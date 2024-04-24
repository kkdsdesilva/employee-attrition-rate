# script for training logistic regression model and evaluating it

# import libraries
import pandas as pd

# import user-defined functions
from data.load import load_data
from data.split import split_data
from data.preprocessing import one_hot_encode
from models.logistic_regression import train_model
from models.evaluation import evaluate_model

# main function
def main():
    ''' Train a logistic regression model and evaluate it
    '''
    
    # load data
    data = load_data(type='general', preprocessed=True)

    # one hot encode for categorical variables
    one_hot_cols = ['Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus']
    data = one_hot_encode(data, one_hot_cols, drop_first=True)
    
    # split data
    X_train, X_test, y_train, y_test = split_data(data, target='Attrition')
    
    # train model
    model = train_model(X_train, y_train)
    
    # predict on test data
    y_pred = model.predict(X_test)
    
    # evaluate model
    evaluation = evaluate_model(y_test, y_pred)
    
    # print evaluation metrics
    print(evaluation)

    # feature importance
    feature_importance = model.coef_[0]
    feature_importance_df = pd.DataFrame({'feature': X_train.columns, 'importance': feature_importance})
    feature_importance_df = feature_importance_df.sort_values(by='importance', ascending=False)
    print(feature_importance_df)

# run the main function
if __name__ == '__main__':
    main()