import requests
from datetime import datetime

from dotenv import load_dotenv
import os

# Get the full path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(script_dir, '..', '.env')
load_dotenv(dotenv_path)

# Access the environment variables
api_key = os.getenv('Nutritionix_api_key')

# Now you can use the api_key in your script
print(api_key)

today = datetime.today()
formatted_date = today.strftime("%d %m %Y").replace(" ", "/")

# Step 1 - set up Nutritionix - it's a free registration

Nutritionix_app_id = os.getenv('Nutritionix_id') #your app id as given by Nutritionix
Nutritionix_api_key = api_key # your api key, provided by Nutritionix

headers = {
    "x-app-id": Nutritionix_app_id,
    "x-app-key": Nutritionix_api_key
}

Nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_input = input ("Tell me which exercises you did: ")

body = {
    "query": user_input
}

response = requests.post(url=Nutritionix_endpoint,json=body, headers=headers)
response_text = response.json()

# Sheety

sheety_endpoint = "https://api.sheety.co/cc24ffa8a724b2ed2db36adc2d9a575c/workoutTracker/workouts"

sheety_token = os.getenv('sheety_api_token') #this is manually made by you when creating the project in Sheety, you can also do no authentication but what fun will that be?

sheety_headers = {
    "Authorization": "Bearer "+sheety_token
}

for exercise in response_text["exercises"]:
    sheety_body = {
    "workout": {
        "date": formatted_date,
        "exercise": response_text["exercises"][0]["name"].title(),
        "duration": response_text["exercises"][0]["duration_min"],
        "calories": response_text["exercises"][0]["nf_calories"]
    }
}
    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_body)
    print (sheety_response.text)