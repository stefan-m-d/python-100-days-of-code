from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Test")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Testington")

email = driver.find_element(By.NAME, "email")
email.send_keys("test@example.com", Keys.ENTER)

time.sleep(10)