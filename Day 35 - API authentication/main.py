import requests

api_key = "" #api key from openweathermap

MY_LAT = 42.681792 # Your latitude
MY_LONG = 23.375497 # Your longitude

params={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

will_rain = False

for item in data["list"]:
    code = item["weather"][0]["id"]
    if int(code)<700:
        will_rain = True
        
if will_rain:
    print("Bring Umbrella")
