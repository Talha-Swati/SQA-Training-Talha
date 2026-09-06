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

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    def go_to_checkout(self):
        if "cart.html" not in self.driver.current_url:
            self.open_cart()
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def get_cart_items(self):
        items = self.wait.until(
            EC.presence_of_all_elements_located(self.cart_items)
        )
        return [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text
            for item in items
        ]

    def remove_item(self, product_name):
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