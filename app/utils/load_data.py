import requests
import pandas as pd

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