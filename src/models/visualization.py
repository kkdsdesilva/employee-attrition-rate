# visualization functions

# import libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc, confusion_matrix, precision_recall_curve
from sklearn.metrics import ConfusionMatrixDisplay, PrecisionRecallDisplay
from sklearn.manifold import TSNE

# function to plot the ROC curve
def plot_roc_curve(model, X_test, y_test, path=None):
    ''' Plot the ROC curve
    Args:
        model (sklearn estimator): Trained model.
        X_test (pandas.DataFrame): Dataframe containing the test data.
        y_test (pandas.Series): Series containing the test target variable.
        '''
    
    # predict probabilities
    y_pred_prob = model.predict_proba(X_test)[:,1]
    
    # calculate the ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    
    # calculate the AUC
    roc_auc = auc(fpr, tpr)
    
    # plot the ROC curve
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')
    if path:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()


# function to plot the precision-recall curve
def plot_precision_recall_curve(model, X_test, y_test, path=None):
    ''' Plot the precision-recall curve
    Args:
        model (sklearn estimator): Trained model.
        X_test (pandas.DataFrame): Dataframe containing the test data.
        y_test (pandas.Series): Series containing the test target variable.
        '''
    
    # predict probabilities
    y_pred_prob = model.predict_proba(X_test)[:,1]
    
    # calculate the precision-recall curve
    precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)

    # plot the precision-recall curve
    plt.figure()
    plt.plot(recall, precision, color='darkorange', lw=2, label='Precision-Recall curve')
    plt.plot([0, 1], [0.5, 0.5], color='navy', lw=2, linestyle='--', label='Random guess')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall curve')
    plt.legend(loc='lower left')
    if path:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()


# function to plot the confusion matrix
def plot_confusion_matrix(model, X_test, y_test, path=None):
    ''' Plot the confusion matrix
    Args:
        model (sklearn estimator): Trained model.
        X_test (pandas.DataFrame): Dataframe containing the test data.
        y_test (pandas.Series): Series containing the test target variable.
        '''
    
    # predict on test data
    y_pred = model.predict(X_test)
    
    # calculate confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # plot the confusion matrix
    fig, ax = plt.subplots(figsize=(6, 4))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No', 'Yes'])
    disp.plot(cmap='Blues', ax=ax)
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title('Confusion Matrix')
    if path:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()


# function to plot feature importance
def plot_feature_importance(model, X, path=None):
    ''' Plot feature importance
    Args:
        model (sklearn estimator): Trained model.
        X (pandas.DataFrame): Dataframe containing the features.
        '''
    
    # get feature importance
    feature_importance = model.feature_importances_
    
    # create dataframe
    feature_importance_df = pd.DataFrame({'feature': X.columns, 'importance': feature_importance})
    feature_importance_df = feature_importance_df.sort_values(by='importance', ascending=False)

    # plot feature importance
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x='importance', y='feature', data=feature_importance_df.iloc[:10])
    plt.title('Feature Importance')
    plt.xlabel('Importance')
    plt.ylabel('Features')
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    plt.tight_layout() 
    if path:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()

# function to plot t-SNE
def plot_tsne(X, y, path=None):
    ''' Plot t-SNE
    Args:
        X (pandas.DataFrame): Dataframe containing the features.
        y (pandas.Series): Series containing the target variable.
        '''
    
    # t-SNE
    tsne = TSNE(n_components=2, random_state=6)
    X_tsne = tsne.fit_transform(X)
    
    # create dataframe
    tsne_df = pd.DataFrame({'X': X_tsne[:, 0], 'Y': X_tsne[:, 1], 'label': y})
    
    # plot t-SNE
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x='X', y='Y', hue='label', data=tsne_df, palette='viridis')
    plt.title('t-SNE')
    if path:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path)
    plt.show()