import re
import pandas as pd
from load_data import fetch_job_listings, convert_to_dataframe
# utils/data_preprocessing.py

# def preprocess_user_preferences(user_preferences):
#     """
#     Preprocess the user preferences before they are fed into the machine learning model.
#     This is just a placeholder function - you'll need to adapt it based on your model's requirements.
#     """
#     # Example: Convert the preferences string to a format your model expects
#     # This could be more complex depending on your model's needs
#     processed_preferences = user_preferences.lower()
#     return processed_preferences

def preprocess_data():
    """
    Preprocesses the job description column of the DataFrame by removing HTML tags.

    This function fetches job listings from an API, converts the JSON data to a pandas DataFrame, and then removes HTML tags 
    from the job descriptions in the DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame containing job listings.

    Returns:
        pandas.DataFrame: DataFrame with preprocessed job descriptions (HTML tags removed).
    """
    # Fetch job listings from the API
    api_url = "https://zobjobs.com/api/jobs"
    json_data = fetch_job_listings(api_url)
    
    # Convert JSON data to a pandas DataFrame
    df = convert_to_dataframe(json_data)

    # Define regular expression pattern to match HTML tags
    html_tags_pattern = re.compile(r'<[^>]+>')

    # Remove HTML tags from job descriptions
    df['description'] = df['description'].apply(lambda x: re.sub(html_tags_pattern, '', x))
    return df