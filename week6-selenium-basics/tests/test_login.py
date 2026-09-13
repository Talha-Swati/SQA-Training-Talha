from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("wrong_user", "wrong_pass")

    assert "Username and password do not match" in login_page.get_error_message()


def test_locked_out_user_cannot_login(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    assert "Sorry, this user has been locked out" in login_page.get_error_message()