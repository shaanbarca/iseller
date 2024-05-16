import requests
from time import sleep
from datetime import datetime as dt
import requests
from time import sleep

def fetch_order(base_url: str, access_token: str, data: dict, retries: int=1):
    '''
    Fetches past order data from a specified API endpoint with retry logic.

    Parameters:
    base_url (str): The API endpoint URL.
    access_token (str): The access token for API authentication.
    data (dict): The payload for the API request.
    retries (int): Number of retry attempts for server errors (default is 1).

    Returns:
    response: HTTP response object if successful, or a string "Failed after multiple retries".
    '''
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    for attempt in range(retries + 1):
        response = requests.post(base_url, headers=headers, data=data)
        if response.status_code == 200:
            return response
        elif response.status_code == 500:
            if attempt < retries:
                print(f"Retry {attempt + 1} of {retries}. Retrying after 5 seconds...")
                sleep(5)
            else:
                return "Failed after multiple retries"
        else:
            print(f"Error fetching data: {response.status_code}")
            return response

    return "Failed after multiple retries"
