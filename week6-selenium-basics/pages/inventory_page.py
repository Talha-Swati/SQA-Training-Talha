from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.products = (By.CLASS_NAME, "inventory_item")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def get_product_count(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.products)
        )
        return len(products)

    def sort_by(self, option):
        dropdown = self.wait.until(
            EC.presence_of_element_located(self.sort_dropdown)
        )

        select = Select(dropdown)
        select.select_by_value(option)

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")

        for product in products:
            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            if name == product_name:
                product.find_element(By.TAG_NAME, "button").click()
                return

    def get_cart_count(self):
        try:
            return int(
                self.wait.until(
                    EC.presence_of_element_located(self.cart_badge)
                ).text
            )
        except:
            return 0