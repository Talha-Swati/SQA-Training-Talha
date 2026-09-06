from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

# Username using ID
username_field = driver.find_element(By.ID, "user-name")
print("Username field found")

# Password using CSS Selector
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
print("Password field found")

# Login button using XPath
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
print("Login button found")

time.sleep(3)

driver.quit()