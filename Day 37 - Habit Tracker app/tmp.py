#I made this to test out some code I found over the internet for the date format, it's not a part of the challenge

from datetime import datetime

today = datetime.today()

formatted_date = today.strftime("%Y %m %d").replace(" ", "")