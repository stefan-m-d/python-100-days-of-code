import requests 
import os
from dotenv import load_dotenv


# Get the full path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(script_dir, '..', '.env')
load_dotenv(dotenv_path)

# Access the environment variables
api_key = os.getenv('sheety_api_token')

#sheety configs

sheety_endpoint = "https://api.sheety.co/cc24ffa8a724b2ed2db36adc2d9a575c/flightDeals/prices"

sheety_token = os.getenv('sheety_api_token') #this is manually made by you when creating the project in Sheety, you can also do no authentication but what fun will that be?

sheety_headers = {
    "Authorization": "Bearer "+sheety_token
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        self.data_dict = self.sheety_response.json()
    
    def get_data(self):
        return self.data_dict
    