from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_full_checkout_flow(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")
    inventory_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = CartPage(driver)
    cart_page.open_cart()
    assert cart_page.get_cart_items() == [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
    ]
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Ali", "Khan", "54000")
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert "Thank you" in checkout_page.get_confirmation_message()


def test_checkout_requires_first_name(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("", "Khan", "54000")
    checkout_page.click_continue()

    assert "First Name is required" in checkout_page.get_error_message()