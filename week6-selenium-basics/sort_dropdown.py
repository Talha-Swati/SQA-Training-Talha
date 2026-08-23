from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

wait = WebDriverWait(driver, 10)

# Login
wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait.until(EC.url_contains("inventory"))

sort_dropdown = Select(
    driver.find_element(By.CLASS_NAME, "product_sort_container")
)

sort_options = [
    "Name (A to Z)",
    "Name (Z to A)",
    "Price (low to high)",
    "Price (high to low)"
]

for option in sort_options:
    sort_dropdown.select_by_visible_text(option)

    first_product_name = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )[0].text

    first_product_price = driver.find_elements(
        By.CLASS_NAME, "inventory_item_price"
    )[0].text

    print("\nSelected:", option)
    print("First product:", first_product_name)
    print("Price:", first_product_price)

driver.quit()