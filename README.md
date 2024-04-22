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

## Model Training

We used two models for this project: a simple logistic regression model and a more robust decision tree model. The decision tree model performed better than the logistic regression model.

To train the decision tree model, run the following command from the project directory:

```bash
python scripts/tree_script.py
```
This script will train the decision tree model and save the model to the models directory.
