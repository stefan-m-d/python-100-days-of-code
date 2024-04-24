import requests
import datetime
import smtplib
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_alphavantage = "" #use your own alphavantage.co api key, it's free and it takes 20 seconds to generate, up to 25 uses per day in free tier
api_key_newsapi = "" #use your own newsapi key
MY_EMAIL = "" #Your email
MY_PASSWORD = "" #Your app password if using Gmail


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


alphavantage_params = {
    "function": "TIME_SERIES_DAILY", #from documentation - this pulls the daily data
    "symbol": STOCK,
    "outputsize": "compact", # from documentation - returns latest 100 datapoints, if set to full, returns full length 20+ years of historical data, so keep this as is!
    "apikey": api_key_alphavantage
}

request_url = "https://www.alphavantage.co/query"

response = requests.get(request_url, params=alphavantage_params)
response.raise_for_status()
data = response.json()
# print (data["Time Series (Daily)"]["2024-04-12"]) # uncomment this if you'd like to check the response given by the API - modify the date to the current one or use var below

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
the_day_before_yesterday = today - datetime.timedelta(days=2)

value_at_open = "1. open" # Dictionary key for stock value when the market opens - obtained from API response
value_at_close = "4. close" # Dictionary key for stock value when the market closes - obtained from API response

stock_price_yesterday = float(data["Time Series (Daily)"][str(yesterday)][value_at_close])
stock_price_day_before_yesterday = float(data["Time Series (Daily)"][str(the_day_before_yesterday)][value_at_close])

def calculate_percentage_change(current_price, previous_price):
    if previous_price==0:
        return 0
    else:
        return ((current_price - previous_price) / previous_price) * 100

try:

    stock_price_today = float(data["Time Series (Daily)"][str(today)][value_at_open]) # if this fails, the market isn't open for today yet
    print (f"Stock price today: {stock_price_today}")
    
    percentage_change = calculate_percentage_change(stock_price_today, stock_price_yesterday)
    percentage_change = round(percentage_change, 2)

except KeyError:  #This means the market isn't opened for the day yet, hence it will get yesterday's data instead
    
    percentage_change = calculate_percentage_change(stock_price_yesterday, stock_price_day_before_yesterday)
    percentage_change = round(percentage_change, 2)
    
    
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


new_params = {
        "q": COMPANY_NAME,  #from documentation
        "language": "en",
        "searchIn": "title,content",
        "from": the_day_before_yesterday,  #this was set to day before yesterday since at the time of coding this, no news about Tesla were out yet and it's 2 AM
        "sortBy": "publishedAt",  #from documentation - this is the param that sorts the news by most recent first
        "apiKey": api_key_newsapi,        
}
    
new_request_url = "https://newsapi.org/v2/everything"
new_response = requests.get(new_request_url, params=new_params)
new_response.raise_for_status()
new_data = new_response.json()

articles = new_data["articles"][:3]

msg_body = '\n'.join([f"{article['source']['name']} \n {article['title']}" for article in articles])


print (msg_body)
    
#The original step 3 was to send an SMS via Twilio's API, but I'd much rather get emails than texts, so I'm doing it via email instead

if percentage_change > 0:
    subject = "Tesla stocks have gone up"
elif percentage_change < 0:
    subject = "Tesla stocks have gone down"
else: 
    subject = "Tesla stocks unchanged"

# if percentage_change > 5 or percentage_change < -5:

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(MY_EMAIL, MY_PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: {subject} \n\nMost recent 3 news about Tesla stocks: \n {msg_body}")
