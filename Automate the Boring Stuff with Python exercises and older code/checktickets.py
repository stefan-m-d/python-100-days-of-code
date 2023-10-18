import ctypes
from selenium import webdriver 
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://www.tomorrowland.com/en/festival/tickets')
elems = browser.find_elements(By.CSS_SELECTOR, '.announcements-3-columns')

all_text=" "

for i in elems:
    newtext = i.text
    all_text=all_text + str(newtext)


if 'SOLD OUT' in all_text:
    browser.quit()
else:
    ctypes.windll.user32.MessageBoxW(0, "Tickets are available", "Available", 0) 
