# utils/model_loading.py

import joblib

def load_recommendation_model(model_path):
    """
    Load the machine learning model for job recommendations.
    """
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None
