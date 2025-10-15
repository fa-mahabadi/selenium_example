from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

webdriver = webdriver.Chrome()
webdriver.maximize_window()
webdriver.get("https://www.google.com")

search_box = webdriver.find_element(By.NAME, "q")
search_box.send_keys("python")
search_box.send_keys(Keys.RETURN)
# assert "python" in webdriver.page_source   -->>  sometime go to delect robote page and not go ro result page
