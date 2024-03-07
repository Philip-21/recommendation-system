import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from data_preprocessing import preprocess_data

def extract_features(df):
    """
    Extracts features from job descriptions using TF-IDF vectorization.

    Args:
        df (pandas.DataFrame): DataFrame containing job listings.

    Returns:
        scipy.sparse.csr_matrix: TF-IDF matrix of job description features.
    """
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['description'])
    return tfidf_matrix

def build_recommender_model(features):
    """
    Builds a recommender model based on cosine similarity.

    Args:
        features (scipy.sparse.csr_matrix): TF-IDF matrix of job description features.

    Returns:
        numpy.ndarray: Cosine similarity matrix of job descriptions.
    """
    cosine_sim = linear_kernel(features, features)
    return cosine_sim

def serialize_model(model, filename):
    """
    Serializes the model to a file using pickle.

    Args:
        model: The model object to be serialized.
        filename (str): The name of the file to which the model will be saved.
    """
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

def main():
    """
    Main function to orchestrate the data preprocessing, model building, and serialization.
    """
    
    # Preprocess job descriptions
    preprocessed_data = preprocess_data()
    
    # Extract features from job descriptions using TF-IDF vectorization
    features = extract_features(preprocessed_data)
    
    # Build a recommender model based on cosine similarity
    model = build_recommender_model(features)
    
    # Serialize the model to a file using pickle
    serialize_model(model, "../../models/recommender_model.pkl")

# Entry point of the script
if __name__ == "__main__":
    main()
