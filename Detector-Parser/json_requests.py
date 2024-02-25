# Requests
import requests
from os import getenv

# URL of the API endpoint and API key
API_URI = getenv("API_URI")
API_KEY = getenv("API_KEY")

# Make sure variables are set
# assert API_KEY is not None
# assert API_URI is not None

# Set the headers to indicate that you're sending JSON data
HEADERS = {'Content-Type': 'application/json'}

def sendDataJSON(json_data: str) -> None:
    # Send a POST request with the JSON data
    response = requests.post(API_URI, data=json_data, headers=HEADERS)

    # Check the response status code
    if response.status_code == 200:
        print("JSON data sent successfully.")
    else:
        print("Error:", response.status_code)
