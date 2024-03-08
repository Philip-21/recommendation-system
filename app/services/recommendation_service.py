# controllers/recommendation_controller.py
import sys
sys.path.append('../utils/')
from ..utils.data_preprocessing import preprocess_data
from ..utils.model_loading import load_recommendation_model
# from ..utils.data_model import User, Job
from fuzzywuzzy import fuzz
from typing import List
import os
import numpy as np

# Load the machine learning model
model_path = os.path.join(os.path.dirname(__file__), '../../models/recommender_model.pkl')
model = None

if os.path.exists(model_path):
    model = load_recommendation_model(model_path)
else:
    print("Model file not found. Please train and save the model first.")

# Load and clean the data from source
df = preprocess_data()

# def get_recommendations(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return []

#     # Preprocess user preferences
#     user_preferences = preprocess_user_preferences(user.job_preferences)

#     # Use the machine learning model to generate recommendations
#     try:
#         recommended_jobs = model.predict([user_preferences])
#     except Exception as e:
#         print(f"Error during model prediction: {e}")
#         return []

#     recommendations = []
#     for job_id in recommended_jobs:
#         job = Job.query.get(job_id)
#         if job:
#             recommendations.append({
#                 'job_id': job.job_id,
#                 'title': job.title,
#                 'description': job.description,
#             })

#     return recommendations

def convert_int64_to_int(data):
    """
    Recursively converts any instances of int64 to int in a nested data structure.

    Parameters:
        data: Any data structure that may contain instances of int64.

    Returns:
        The input data structure with int64 instances converted to int.

    Note:
        This function recursively traverses a nested data structure and converts
        any instances of int64 to int. It supports dictionaries, lists, and single
        int64 values.
    """
    if isinstance(data, dict):
        # If data is a dictionary, convert each value recursively
        return {key: convert_int64_to_int(value) for key, value in data.items()}
    elif isinstance(data, list):
        # If data is a list, convert each item recursively
        return [convert_int64_to_int(item) for item in data]
    elif isinstance(data, np.int64):
        # If data is an int64, convert it to int
        return int(data)
    else:
        # If data is neither a dictionary nor a list nor an int64, return it as is
        return data
    
def get_recommendations(job_title, df, model, top_n=5):
    """
    Generates recommendations based on a given job title.

    Args:
        job_title (str): The title of the job to generate recommendations for.
        df (pandas.DataFrame): DataFrame containing job listings.
        model (numpy.ndarray): Cosine similarity matrix of job descriptions.
        top_n (int): Number of recommendations to generate.

    Returns:
        list: List of dictionaries containing recommended job details.
    """
    if len(df) == 0:
        print("DataFrame is empty. Unable to make recommendations.")
        return None
    # Calculate similarity scores between the input job title and all job titles in the DataFrame
    similarity_scores = df['title'].apply(lambda x: fuzz.token_sort_ratio(job_title.lower(), x.lower()))
    # Get the index of the job title with the highest similarity score
    idx = similarity_scores.idxmax()
    # Use the index to get recommendations based on the model
    sim_scores = list(enumerate(model[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    job_indices = [i[0] for i in sim_scores]
    # Retrieve other required fields using the indices of recommended jobs
    recommendations = []
    for index in job_indices:
        job_id = df.loc[index, 'unique']
        title = df.loc[index, 'title']
        description = df.loc[index, 'description']
        recommendations.append({
            'job_id': job_id,
            'title': title,
            'description': description
        })
    return recommendations


# job_title = "Wordpress Developer"
# recommended_jobs = get_recommendations(job_title, preprocessed_data, loaded_model)
# if recommended_jobs is not None:
#     print("Recommended Jobs for {}: \n{}".format(job_title, recommended_jobs))

