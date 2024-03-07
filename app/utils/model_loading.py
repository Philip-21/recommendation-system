import pickle
    
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
