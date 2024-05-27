#this was originally planned for Amazon, but I don't normally shop from there, so I've modified it to a local Bulgaria supplier instead

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import datetime

cwd = os.getcwd()

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(cwd, 'Python.env')
load_dotenv(dotenv_path)

headers = {
    'Accept-Language' : "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
}

URL = "https://www.ozone.bg/product/playstation-5-group-model-slim/" #change this to something else if you wish to track something else

s = requests.Session()
s.headers.update(headers)

response = s.get(URL, headers=headers)

html = response.text

soup = BeautifulSoup(html, "html.parser")

price = soup.select_one('div.price-box')

ozone_price = price.getText().replace("\n", "")

#I use sheety to make a price tracker throughout the year since there have been a lot of speculations about whether or not prices actually go down during Black Friday here

sheety_endpoint = os.getenv('sheety_endpoint_price')

sheety_token = os.getenv('sheety_api_token')

sheety_headers = {
    "Authorization": "Bearer "+sheety_token.strip('\"')
}

today = datetime.datetime.today()
formatted_date = today.strftime("%d %m %Y").replace(" ", "/")

sheety_body = {
    "price": {
        "date": formatted_date,
        "price": ozone_price
        }
    }

sheety_response = requests.post(url=sheety_endpoint.strip('\"'), headers=sheety_headers, json=sheety_body) # we actually need the strip('\"') part here as otherwise, dockerizing this app fails because of the connection endpoint being interpreted with the quotes because of the .env file. 
sheety_response.raise_for_status()