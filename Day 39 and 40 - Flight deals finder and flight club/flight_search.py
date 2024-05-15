import requests 

serp_api_endpoint = "https://serpapi.com/search?engine=google_flights"

search_params = {
            "engine": "google_flights",
            "hl": "en",
            "gl": "us",
            "type": "1",
            "departure_id": "SOF",
            "arrival_id": "STN",
            "outbound_date": "2024-05-23",
            "return_date": "2024-05-30",
            "adults": 2,
            "max_price": "250",
            "show_hidden": "true",
            "api_key": "",
            "currency": "EUR"
            }


results = requests.get(url=serp_api_endpoint, json=search_params)
print (results.text)
data = results.json()
print (data)


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass