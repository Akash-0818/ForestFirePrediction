import pickle
import os

def load_model():
    # Get the absolute path to the Models folder
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    models_dir = os.path.join(base_dir, 'Models')
    
    # Full path to the pickle file
    model_path = os.path.join(models_dir, 'model_rsearchcv.pickle')
    
    # Load the model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    return model
