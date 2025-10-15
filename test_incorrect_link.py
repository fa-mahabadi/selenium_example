from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://realpython.com/")
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    url = link.get_attribute("href")
    if url:
        response = requests.head(url)
        # print(response)       #display status_code all link
        if response.status_code != 200:
            print(url)          # display all link address non-200