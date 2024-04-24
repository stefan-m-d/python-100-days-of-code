import smtplib
import random
import datetime as dt

#some assembly required - setup the vars below with App passwords for Gmail

my_email=""
password=""
weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
path = "Day 32 - Automated happy birthday emails\quotes.txt"

#Open file to get quotes as list

quotes=""
with open (path) as file:
    quotes=file.readlines()
    file.close()

#Get random quote

random_quote = random.choice(quotes)

#Get current day of the week

now = dt.datetime.now()
day = now.weekday()

#Send email - setup the to_addrs var, please, otherwise it won't work. 

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:{weekdays[day]} motivational quote\n\n{random_quote}")
