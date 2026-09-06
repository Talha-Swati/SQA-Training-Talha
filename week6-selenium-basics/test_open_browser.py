from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com")

print("Page title:", driver.title)

time.sleep(3)

driver.quit()