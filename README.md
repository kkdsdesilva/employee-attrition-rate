# Technical Assessment

To replicate the results of this project, please follow the instructions below.

## Installation
To install the dependencies for this project, please refer to the requirements.txt file. It contains a list of all the required packages and their versions.

You can install the dependencies by running the following command:
```bash
pip install -r requirements.txt
```

To install this project in editable mode, navigate to the project directory and run the following command:

```bash
pip install -e .
```

## Model Training and Hyperparameter Tuning

We used 3 models for this project: a simple logistic regression model, a more robust decision tree model and a random forest model. Since both decision tree and random forest models outperformed the logistic regression model, we will focus on the decision tree and random forest models.

### Decision Tree Model

To tune hyperparameters for the decision tree model, run the following command:

```bash
python scripts/tree_tuning_script.py
```

This script will perform hyperparameter tuning using grid search and save the best model in the models directory and save the grid search results in the metrics directory.

To train and evaluate the decision tree model, run the following command:

```bash
python scripts/tree_script.py
```

This script will train the decision tree model and save confusion matrix, feature importance, roc curve, and precision-recall curve plots in the reports/figures directory.

### Random Forest Model

To tune hyperparameters for the random forest model, run the following command:

```bash
python scripts/forest_tuning_script.py
```

This script will perform hyperparameter tuning using grid search and save the best model in the models directory and save the grid search results in the metrics directory.

To train and evaluate the random forest model, run the following command:

```bash
python scripts/forest_script.py
``` 

This script will train the random forest model and save confusion matrix, feature importance, roc curve, and precision-recall curve plots in the reports/figures directory.

