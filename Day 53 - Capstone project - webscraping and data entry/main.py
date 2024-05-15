from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

FORM_URL = "https://forms.gle/E79FWxHVCrRGvUer5"
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    'Accept-Language' : "en-US,en;q=0.9",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
}

s = requests.Session()
s.headers.update(headers)

response = s.get(ZILLOW_CLONE_URL, headers=headers)

html = response.text
soup = BeautifulSoup(html, "html.parser")

#get all addresses in a list

addresses = []

for tag in soup.select("a.StyledPropertyCardDataArea-anchor address"):
    text = tag.text.replace("\n", "").replace("                                ", "")
    addresses.append(text)

# get all prices in a list

prices = []

for tag in soup.select("span.PropertyCardWrapper__StyledPriceLine"):
    prices.append(tag.text.replace("1 bd", "").replace("/mo", ""))

#get all links in a list

links = []

for tag in soup.select("a.property-card-link"):
    links.append(tag.get("href"))

# time for Selenium to write all this stuff in the form 

driver = webdriver.Chrome()

driver.get(FORM_URL)

for n in range(len(addresses)):
    
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[n])

    price = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    price.send_keys(prices[n])

    link = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    link.send_keys(links[n])

    send_response = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span")
    send_response.click()

    #putting this here for loading times purposes
    
    time.sleep(0.5)
    
    send_another_response = driver.find_element(By.CSS_SELECTOR, "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a")
    send_another_response.click()

driver.quit()