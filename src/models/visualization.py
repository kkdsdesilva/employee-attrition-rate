# visualization functions

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc, confusion_matrix, precision_recall_curve

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
    plt.show()

    if path:
        plt.savefig(path)

# function to plot the precision-recall curve
def plot_precision_recall_curve(model, X_test, y_test):
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
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall curve')
    plt.legend(loc='lower left')
    plt.show()

    if path:
        plt.savefig(path)

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
    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.show()

    if path:
        plt.savefig(path)


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
    plt.figure()
    sns.barplot(x='importance', y='feature', data=feature_importance_df)
    plt.title('Feature Importance')
    plt.show()

    if path:
        plt.savefig(path)

