#this test script tests the main.py file from the PriceTracker directory. It should be in the same location as the Python.env file as it depends on it to run. 
# Otherwise it causes errors generating the Sheety parameters, which are responsible for the API call

from PriceTracker.main import *

def test_vars_loaded_from_env_file():
    assert sheety_endpoint is not None, "Endpoint is incorrect, please check .env file"
    assert sheety_token is not None, "Sheety Token env var is not correctly loaded, API requests unavailable"

def test_api_connectivity():
    assert "200" in str(sheety_response), "Post request failed"

def test_spreadsheet_data():
    data = requests.get(url=sheety_endpoint.strip('\"'), headers=sheety_headers, json=sheety_body)
    assert data.json() is not None, "Spreadsheet data is empty"
    
def test_scrape_price():
    assert ozone_price is not None, "Scraped price is incorrect, please check selector"
    assert soup is not None, "Retrieved HTML code is empty"
    assert "." in str(ozone_price), "Retrieved price is not correct, please check selector"
    
def test_data_sent_to_spreadsheet():
    assert sheety_body["price"]["date"] is not None, "Date sent to spreadsheet is empty"
    assert sheety_body["price"]["price"] is not None, "Price sent to spreadsheet is empty"

