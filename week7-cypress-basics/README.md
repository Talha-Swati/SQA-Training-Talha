# Week 7 - Cypress Basics

First look at Cypress. Converted 3 of the Week 6 Selenium login tests over to it so I could compare the two directly instead of just reading about the differences.

## Setup

```bash
npm install
npx cypress open        # interactive test runner
npx cypress run --spec "cypress/e2e/login.cy.js"   # headless, used for timing below
```

## What's in here

- `cypress.config.js` - baseUrl set to saucedemo.com so tests don't repeat the URL every time
- `cypress/e2e/login.cy.js` - the 3 converted tests
- rest is just the default Cypress scaffold (`support/`, `fixtures/`)

## Tests (converted from week6/tests/test_login.py)

1. Valid login -> ends up on the inventory page
2. Invalid login -> shows "Username and password do not match"
3. Locked out user -> shows "Sorry, this user has been locked out"

All 3 pass.

## Cypress vs Selenium - what I noticed

- No more `WebDriverWait` everywhere. `cy.get()` just retries on its own until the element shows up.
- Cypress runs in the same process as the browser instead of talking to it through a driver, so when something fails the error points straight at the command, not a WebDriver stack trace.
- Selenium's fixture opens a brand new Chrome window for every test. Cypress kept one browser open for all 3 tests in the file - that's the main reason it's faster (see below).
- Less boilerplate to write. `cy.get('#user-name').type(...)` vs `driver.find_element(By.ID, "user-name").send_keys(...)`.
- Assertions chain right onto the command (`.should(...)`) instead of a separate `assert` line after.

## Speed

Same 3 scenarios, both against the live SauceDemo site:

- Selenium (`test_login.py`, pytest): **31s** for 3 tests - new Chrome window each time
- Cypress (`login.cy.js`): **5-6s** for 3 tests - one browser reused for the whole file

Cypress was roughly 5x faster here. Mostly comes down to not relaunching the browser between tests - the actual typing/clicking/asserting speed felt about the same in both.
