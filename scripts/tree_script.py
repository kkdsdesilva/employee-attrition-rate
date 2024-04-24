# script for training decision tree model and evaluating it

# import libraries
import pandas as pd
import os

# import user-defined functions
from data.load import load_data
from data.split import split_data
from data.preprocessing import one_hot_encode
from models.decision_tree import train_model
from models.evaluation import evaluate_model
from models.visualization import plot_feature_importance,  plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve

# root directory
cur_dir = os.path.dirname(__file__) # current directory
root_dir = os.path.abspath(os.path.join(cur_dir, '..')) # root directory

# main function
def main():
    ''' Train a decision tree model and evaluate it
    '''
    
    # load data
    data = load_data(type='general', preprocessed=True)

    # one hot encode for categorical variables
    one_hot_cols = ['Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus']
    data = one_hot_encode(data, one_hot_cols, drop_first=False)

    # split data
    X_train, X_test, y_train, y_test = split_data(data, target='Attrition', test_size=0.2)

    # best hyperparameters
    params = {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 2}

    # train model
    model = train_model(X_train, y_train, **params)

    # plot feature importance
    plot_feature_importance(model, X_train, root_dir+'/reports/figures/tree_feature_importance.png', title='Decision Tree Feature Importance')

    # plot confusion matrix
    plot_confusion_matrix(model, X_test, y_test, root_dir+'/reports/figures/tree_confusion_matrix.png')
    
    # plot ROC curve
    plot_roc_curve(model, X_test, y_test, root_dir+'/reports/figures/tree_roc_curve.png')

    # plot precision-recall curve
    plot_precision_recall_curve(model, X_test, y_test, root_dir+'/reports/figures/tree_precision_recall_curve.png')


# run the main function
if __name__ == '__main__':
    main()