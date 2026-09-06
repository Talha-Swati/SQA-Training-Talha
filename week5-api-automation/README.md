# Week 5 API Automation Framework

This project is a simple API automation testing framework built using Python, Requests, and Pytest. It tests ReqRes API CRUD operations and login functionality using reusable helper functions, parameterized test data, assertions, and HTML reporting.

## Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

## Run Tests

Run the complete test suite and generate the HTML report:

```bash
pytest -v --html=report.html
```

## Project Structure

```text
week5-api-automation/
│
├── config.py
├── api_helpers.py
├── test_users_api.py
├── test_data.json
├── requirements.txt
├── README.md
├── report.html
└── assets/
    └── style.css
```

### config.py

Stores common configuration such as the API base URL, request headers, API key, and timeout settings.

### api_helpers.py

Contains reusable API request functions for GET, POST, PUT, DELETE, and login requests.

### test_users_api.py

Contains the Pytest test cases for user CRUD operations and login scenarios. It also uses parameterization to run multiple test cases with different data.

### test_data.json

Stores external test data used by parameterized POST tests.

### requirements.txt

Contains the Python packages required to install and run the automation framework.

### report.html

Contains the HTML test execution report generated using pytest-html.

## Test Coverage

The framework covers:

* GET list of users
* GET valid single user
* GET invalid user
* POST create user
* PUT update user
* DELETE user
* Successful login
* Login with missing password

The final test execution contains 16 test cases and all tests pass successfully.
