from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        print("Loading SauceDemo login page")
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        print(f"Logging in as {username}")
        self.wait.until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        message = self.wait.until(
            EC.presence_of_element_located(self.error_message)
        ).text
        print(f"Login error message: {message}")
        return message