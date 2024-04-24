import random
import smtplib
import pandas
import datetime as dt

#fill below 2 vars with email you'll send from and an App Password if using a Gmail address
my_email=""
password=""

bday_path="Day 32 - Automated happy birthday emails/birthdays.csv"

df = pandas.read_csv(bday_path)
bday_dict = df.to_dict(orient="records")

now = dt.datetime.now()
day = now.day
month=now.month

for row in bday_dict:
    template_choice = f"Day 32 - Automated happy birthday emails/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(template_choice) as file:
        template=file.readlines()
        bday_wish = "".join(n for n in template)
    if row["month"] == month and row["day"] == day:
        bday_wish = bday_wish.replace("[NAME]", row["name"])
        print(bday_wish)
        print(row["email"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row["email"], msg=f"Subject:Happy birthday\n\n{bday_wish}")



