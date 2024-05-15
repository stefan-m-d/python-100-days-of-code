from data_manager import DataManager
import flight_data
import flight_search
import notification_manager
import os
from dotenv import load_dotenv

# Get the full path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(script_dir, '..', '.env')
load_dotenv(dotenv_path)

# Access the environment variables
api_key = os.getenv('sheety_api_token')

#get Google Sheet Data

data_manager = DataManager()
data = data_manager.get_data()
print (data)