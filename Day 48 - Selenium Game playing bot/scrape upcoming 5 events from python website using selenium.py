from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org")

events = {}

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')


# for event in event_times:
#     datetime = event.get_attribute("datetime")
#     print (datetime[0:10]) - this gets just the date from the entire datetime tag
# #    print (event.text) - this doesn't work - there are 2 classes for the time, so the date is actually obtained from the datetime property

# for name in event_names:
#     print (name.text)
    
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].get_attribute("datetime")[0:10],
        "name": event_names[n].text 
    }

print (events)