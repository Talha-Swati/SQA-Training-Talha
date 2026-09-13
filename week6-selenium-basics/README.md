# Week 6 Selenium Automation Suite

This project is a Selenium-based UI automation suite built using Python, Selenium WebDriver, and Pytest. It tests the SauceDemo (`https://www.saucedemo.com`) login, inventory, cart, and checkout flows using the Page Object Model (POM), reusable page classes, assertions, and HTML reporting.

## Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

## Run Tests

Run the complete test suite and generate the HTML report:

```bash
pytest tests/ -v --html=report.html
```

## Project Structure

```text
week6-selenium-basics/
│
├── conftest.py
├── requirements.txt
├── README.md
├── report.html
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
└── tests/
    ├── test_login.py
    ├── test_inventory.py
    └── test_checkout_flow.py
```

### conftest.py

Provides the shared `driver` pytest fixture that launches and quits the Chrome WebDriver for every test.

### pages/

Contains the Page Object Model (POM) classes, one per SauceDemo page. POM was used so that locators and page interactions live in a single place per page instead of being duplicated across tests. Each test then reads like a sequence of user actions (`login_page.login(...)`, `cart_page.open_cart()`) rather than raw Selenium calls, which makes tests easier to read and update — if a locator changes, only the page object needs to change, not every test that uses it. Every page object method also prints a short log line for its key action (e.g. `Logging in as {username}`, `Adding '{product}' to cart`), which makes it much faster to see where a chained flow failed.

* **login_page.py** — loads the login page, submits credentials, and reads login error messages.
* **inventory_page.py** — reads product listings, sorts products, adds a product to the cart by name, and reads the cart badge count.
* **cart_page.py** — opens the cart, reads cart contents, removes items, returns to the inventory via "Continue Shopping", and proceeds to checkout.
* **checkout_page.py** — fills in checkout information, continues/finishes checkout, and reads confirmation/error messages.

### tests/

Contains the Pytest test cases, grouped by feature area.

### requirements.txt

Contains the Python packages required to install and run the automation suite.

### report.html

Contains the HTML test execution report generated using pytest-html.

## Test Coverage

The suite covers:

* Valid login
* Invalid login (wrong username/password)
* Locked-out user login (`locked_out_user` gets blocked with a "Sorry, this user has been locked out" error)
* Full checkout flow: add products to cart, verify cart contents, fill checkout info, complete the order
* Checkout validation: checkout is rejected when first name is missing
* Checkout with an empty cart: SauceDemo does **not** block this — clicking "Checkout" on an empty cart still proceeds to the checkout info form with nothing to buy
* Sort persistence through navigation: sorting by "Price (low to high)", then visiting the cart and returning to inventory via "Continue Shopping", resets the sort back to the default "Name (A to Z)" order — the sort selection does **not** persist

The final test execution contains 7 test cases and all tests pass successfully.
