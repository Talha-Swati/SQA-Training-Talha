from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

# Add 3 products
driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
).click()

driver.find_element(
    By.ID, "add-to-cart-sauce-labs-bike-light"
).click()

driver.find_element(
    By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
).click()

# Verify cart count
cart_count = wait.until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "shopping_cart_badge")
    )
)

print("Cart count after adding products:", cart_count.text)

assert cart_count.text == "3"

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

wait.until(EC.url_contains("cart"))

# Get product names
cart_products = driver.find_elements(
    By.CLASS_NAME, "inventory_item_name"
)

print("\nProducts in cart:")

for product in cart_products:
    print("-", product.text)

assert len(cart_products) == 3

# Remove one product
driver.find_element(
    By.ID, "remove-sauce-labs-backpack"
).click()

# Verify updated cart count
wait.until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "shopping_cart_badge"),
        "2"
    )
)

updated_count = driver.find_element(
    By.CLASS_NAME, "shopping_cart_badge"
).text

print("\nCart count after removing one product:", updated_count)

assert updated_count == "2"

driver.quit()