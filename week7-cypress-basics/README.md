# Week 7 Cypress Basics

This project is a Cypress-based UI automation suite for the SauceDemo (`https://www.saucedemo.com`) login flow. It converts 3 of the simplest Week 6 Selenium tests (valid login, invalid login, locked-out user) into Cypress, so the two tools can be compared directly on the same scenarios.

## Install Dependencies

Run:

```bash
npm install
```

## Run Tests

Open the interactive Cypress Test Runner (pick `E2E Testing`, choose a browser, then click `login.cy.js`):

```bash
npx cypress open
```

Run headlessly from the CLI (used for the timing comparison below):

```bash
npx cypress run --spec "cypress/e2e/login.cy.js"
```

## Project Structure

```text
week7-cypress-basics/
│
├── cypress.config.js
├── package.json
├── README.md
├── cypress/
│   ├── e2e/
│   │   └── login.cy.js
│   ├── fixtures/
│   │   └── example.json
│   └── support/
│       ├── commands.js
│       └── e2e.js
```

### cypress.config.js

Configures Cypress's e2e testing mode and sets `baseUrl` to `https://www.saucedemo.com`.

### cypress/e2e/login.cy.js

Contains the 3 converted test cases, described below.

## Test Coverage

Converted from `week6-selenium-basics/tests/test_login.py`:

* Valid login (`standard_user` / `secret_sauce`) redirects to the inventory page
* Invalid login (wrong username/password) shows the "Username and password do not match" error
* Locked-out user (`locked_out_user` / `secret_sauce`) shows the "Sorry, this user has been locked out" error

All 3 tests pass.

## Cypress vs Selenium — Observations

Having now written the same 3 login tests in both tools, a few things stood out:

1. **No explicit waits needed.** In Selenium every element lookup went through a `WebDriverWait` + `expected_conditions` call in the page objects. In Cypress, `cy.get(...)` just retries automatically until the element appears (or times out), so none of that wrapper code was necessary.
2. **Tests run inside the browser, not through a separate driver.** Selenium talks to Chrome through the ChromeDriver process over a wire protocol; Cypress's test code executes directly in the same run loop as the browser, which is also why its error messages and command log point straight at the failing step instead of a WebDriver stack trace.
3. **One browser, many tests.** Selenium's `driver` fixture launches a brand-new Chrome window for every single test, while all 3 Cypress tests ran in one shared Electron browser instance for the whole spec file — this is the single biggest reason the Cypress run was faster (see timing below).
4. **Syntax is shorter and reads more like the DOM.** `cy.get('#user-name').type(...)` versus `driver.find_element(*locator).send_keys(...)` — Cypress's jQuery-like chaining removed a lot of the `By.ID` / tuple-locator boilerplate that the Selenium page objects needed.
5. **Assertions are built into the chain.** `.should('include', ...)` reads as part of the same command chain, whereas Selenium needed a separate `assert` statement after fetching the value with a page-object method.

## Speed Comparison

Both runs cover the same 3 scenarios (valid login, invalid login, locked-out user) against the live SauceDemo site.

| Suite | Tool | Browser strategy | Reported test time |
|---|---|---|---|
| `week6-selenium-basics/tests/test_login.py` | Selenium + pytest | New Chrome window per test (function-scoped `driver` fixture) | **31.04s** for 3 tests (`pytest -v`) |
| `week7-cypress-basics/cypress/e2e/login.cy.js` | Cypress | One shared headless Electron browser for the whole spec | **5–6s** for 3 tests (Cypress's own reported spec duration; `npx cypress run` wall-clock including Electron startup was ~20s) |

Cypress's actual test execution was roughly **5x faster** than Selenium for the same 3 scenarios. Most of that gap comes from Selenium re-launching a full Chrome instance for every test, while Cypress reuses one browser across the whole file — the per-command speed (typing, clicking, asserting) is fast in both tools, but browser startup dominates the Selenium timing here.
