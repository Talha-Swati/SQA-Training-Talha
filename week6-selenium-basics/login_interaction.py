from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

login_button.click()

time.sleep(2)

print("Current URL after login:", driver.current_url)

driver.quit()