import re
import pandas as pd
# from load_data import fetch_job_listings, convert_to_dataframe
import requests

def fetch_job_listings(api_url):
    """
    Fetches job listings from the specified API URL.

    Args:
        api_url (str): The URL of the API endpoint.

    Returns:
        list: A list of job listings retrieved from the API.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['jobs']
    else:
        print("Error fetching job listings:", response.status_code)
        return None

def convert_to_dataframe(json_data):
    """
    Converts JSON data into a pandas DataFrame.

    Args:
        json_data (list): List of JSON objects representing job listings.

    Returns:
        pandas.DataFrame: DataFrame containing job listings.
    """
    df = pd.DataFrame(json_data)
    return df

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