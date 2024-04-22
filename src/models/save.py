# saving the model

# import libraries
import joblib

# function to save the model
def save_model(model, path):
    ''' Save the model
    Args:
        model (sklearn estimator): Trained model to be saved.
        path (str): Path where the model will be saved.
        '''
    
    joblib.dump(model, path)
    
    return