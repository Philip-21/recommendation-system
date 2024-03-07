import re
import pandas as pd
from load_data import fetch_job_listings, convert_to_dataframe

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