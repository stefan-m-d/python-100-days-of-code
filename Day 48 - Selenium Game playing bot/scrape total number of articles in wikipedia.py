from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element(By.ID, "articlecount")
print (number_of_articles.text)