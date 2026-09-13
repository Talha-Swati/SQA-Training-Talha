from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")

    def open_cart(self):
        print("Opening cart")
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()
        self.wait.until(EC.url_contains("cart.html"))

    def continue_shopping(self):
        print("Returning to inventory from cart")
        self.wait.until(
            EC.element_to_be_clickable(self.continue_shopping_button)
        ).click()
        self.wait.until(EC.url_contains("inventory.html"))

    def go_to_checkout(self):
        print("Going to checkout")
        if "cart.html" not in self.driver.current_url:
            self.open_cart()
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def get_cart_items(self):
        self.wait.until(EC.url_contains("cart.html"))
        # find_elements (not presence_of_all_elements_located) is used here
        # because the cart can legitimately be empty, and that EC treats an
        # empty list as falsy and times out instead of returning [].
        items = self.driver.find_elements(*self.cart_items)
        names = [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text
            for item in items
        ]
        print(f"Cart items: {names}")
        return names

    def remove_item(self, product_name):
        print(f"Removing '{product_name}' from cart")
        items = self.driver.find_elements(*self.cart_items)

        for item in items:
            name = item.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            if name == product_name:
                item.find_element(
                    By.TAG_NAME,
                    "button"
                ).click()
                return