# Week 7 - Cypress Basics

Day 1: first look at Cypress, converted 3 of the Week 6 Selenium login tests over to compare the two directly.
Day 2: fixtures, a data-driven test, and a custom command.

## Setup

```bash
npm install
npx cypress open        # interactive test runner
npx cypress run          # headless, runs everything in cypress/e2e
```

## What's in here

- `cypress.config.js` - baseUrl set to saucedemo.com so tests don't repeat the URL every time
- `cypress/fixtures/users.json` - login credentials for the 3 login scenarios
- `cypress/fixtures/products.json` - product names for the data-driven cart test
- `cypress/support/commands.js` - custom `cy.login(username, password)` command
- `cypress/e2e/login.cy.js` - login tests, pulling data from `users.json`
- `cypress/e2e/cart.cy.js` - loops through `products.json` and adds each one to the cart
- rest is just the default Cypress scaffold

## Tests

`login.cy.js` (converted from week6/tests/test_login.py, now fixture-driven):
1. Valid login -> ends up on the inventory page
2. Invalid login -> shows "Username and password do not match"
3. Locked out user -> shows "Sorry, this user has been locked out" (checked the exact wording on the live site first - full message is "Epic sadface: Sorry, this user has been locked out.")

`cart.cy.js`:
4. Reads 3 product names from `products.json`, adds each to the cart by clicking `[data-test="add-to-cart-<slug>"]` (slug = product name lowercased, spaces to hyphens - matches the site's actual attribute), then checks the cart badge equals 3

All 4 pass.

## Fixtures

Same idea as `test_data.json` in the Week 5 API framework - keep test data out of the test file itself. `cy.fixture('users').as('users')` loads the JSON and makes it available as `this.users` inside the test (needs a regular `function () {}`, not an arrow function, since `this` binding is how Cypress attaches aliases).

## Custom command

Every test needs to log in first, so that's now `cy.login(username, password)` in `cypress/support/commands.js` instead of repeating visit/type/type/click in every test. All 4 tests use it now.

## Cypress vs Selenium - what I noticed (from Day 1)

- No more `WebDriverWait` everywhere. `cy.get()` just retries on its own until the element shows up.
- Cypress runs in the same process as the browser instead of talking to it through a driver, so when something fails the error points straight at the command, not a WebDriver stack trace.
- Selenium's fixture opens a brand new Chrome window for every test. Cypress kept one browser open for all tests in a file - that's the main reason it's faster (see below).
- Less boilerplate to write. `cy.get('#user-name').type(...)` vs `driver.find_element(By.ID, "user-name").send_keys(...)`.
- Assertions chain right onto the command (`.should(...)`) instead of a separate `assert` line after.

## Speed

Same 3 login scenarios, both against the live SauceDemo site:

- Selenium (`test_login.py`, pytest): **31s** for 3 tests - new Chrome window each time
- Cypress (`login.cy.js`): **5-6s** for 3 tests - one browser reused for the whole file

Cypress was roughly 5x faster here. Mostly comes down to not relaunching the browser between tests - the actual typing/clicking/asserting speed felt about the same in both.
