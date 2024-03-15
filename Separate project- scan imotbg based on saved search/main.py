import pandas as pd
import os
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By

#open browser
browser = webdriver.Edge()
browser.get('https://www.imot.bg/pcgi/imot.cgi?act=26&logact=1')
browser.maximize_window()

#agree to cookies
to_site_btn = browser.find_element(By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button')
to_site_btn.click()

#select private entity radio btn
private_entity = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(3) > div > div.formsWrapper > ul > li.left > form > div.vhodOptions > label:nth-child(2)')
private_entity.click()

username = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(3) > div > div.formsWrapper > ul > li.left > form > input[type=text]:nth-child(6)')
password = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(3) > div > div.formsWrapper > ul > li.left > form > input[type=password]:nth-child(7)')
remember = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(3) > div > div.formsWrapper > ul > li.left > form > label:nth-child(8) > input[type=checkbox]')
log_in_btn = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(3) > div > div.formsWrapper > ul > li.left > form > a.loginButton')

#log in, uncheck remember me box
username.click()
username.send_keys("ninjaiscrazy@gmail.com")
password.click()
password.send_keys("Awesome3!")
remember.click()
log_in_btn.click()

#open saved search
gui_filters = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div.submenu > a:nth-child(3) > span')
gui_filters.click()

gui_do_search = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div:nth-child(4) > div.myFilterItem > div:nth-child(2) > a')
gui_do_search.click()

time.sleep(7)


number_of_ads = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(2) > table:nth-child(10) > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(2)')


most_recent_ad_price = browser.find_element(By.CLASS_NAME, 'price')
most_recent_ad_location = browser.find_element(By.CSS_SELECTOR, 'body > div:nth-child(2) > table:nth-child(10) > tbody > tr:nth-child(1) > td:nth-child(1) > table:nth-child(12) > tbody > tr:nth-child(2) > td:nth-child(2) > a.lnk2')

print(number_of_ads.get_attribute("text"))
print(most_recent_ad_location.get_attribute("text")) #this works!
print(most_recent_ad_price.get_attribute("text"))


os.system("pause")