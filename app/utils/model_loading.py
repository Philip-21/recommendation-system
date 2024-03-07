# utils/model_loading.py

# import joblib
import pickle

# def load_recommendation_model(model_path):
#     """
#     Load the machine learning model for job recommendations.
#     """
#     try:
#         model = joblib.load(model_path)
#         return model
#     except Exception as e:
#         print(f"Error loading the model: {e}")
#         return None
    
def load_recommendation_model(filename):
    """
    Deserializes the model from a pickled file.

    Args:
        filename (str): The name of the pickled file containing the model.

    Returns:
        object: The deserialized model object.
    """
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    return model
