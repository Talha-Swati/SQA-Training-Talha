from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_sort_does_not_persist_through_cart_navigation(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.sort_by("lohi")
    sorted_names = inventory_page.get_product_names()

    inventory_page.add_product_to_cart(sorted_names[0])

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.continue_shopping()

    # Actual SauceDemo behavior: navigating to the cart and back to
    # inventory resets the sort dropdown to its default "Name (A to Z)"
    # value, it does not remember the "Price (low to high)" selection.
    names_after_return = inventory_page.get_product_names()
    assert names_after_return == sorted(names_after_return)
    assert names_after_return != sorted_names
