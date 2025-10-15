from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("student")
password.send_keys("Password123")
button = driver.find_element(By.ID, "submit")
button.click()
assert (
    "https://practicetestautomation.com/logged-in-successfully/" in driver.current_url
)
print(driver.current_url)
