from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.confirmation_message = (By.CLASS_NAME, "complete-header")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        print(f"Filling checkout info: {first_name} {last_name}, {zip_code}")
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def click_continue(self):
        print("Clicking continue")
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def click_finish(self):
        print("Clicking finish")
        self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()

    def get_confirmation_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.confirmation_message)
        ).text
        print(f"Checkout confirmation message: {message}")
        return message

    def get_error_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text
        print(f"Checkout error message: {message}")
        return message