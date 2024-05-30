from selenium import webdriver
from selenium.webdriver.common.by import By

#these 2 rows keep Chrome opened

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://allgsm.eu/sony-playstation-5-slim-1tb-disc-edition")

price_bgn = driver.find_element(By.CSS_SELECTOR, "span.price.new-price.new-price-m")

print (price_bgn.text)