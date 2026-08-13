import requests
API_KEY = "free_user_3HX1rLoxrzgyA5WpxMc3rpqcUle"
headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

def test_get_users_list():
    response = requests.get(
        "https://reqres.in/api/users?page=2",
        headers=headers
    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"

    print("PASS: test_get_users_list")


def test_get_single_user():
    response = requests.get(
        "https://reqres.in/api/users/2",
        headers=headers
    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"

    data = response.json()

    assert data["data"]["id"] == 2, \
        "User ID doesn't match"

    assert "email" in data["data"], \
        "Email field is missing"

    print("PASS: test_get_single_user")


def test_get_non_existent_user():
    response = requests.get(
        "https://reqres.in/api/users/999",
        headers=headers
    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 404, \
        f"Expected 404, got {response.status_code}"

    print("PASS: test_get_non_existent_user")


def test_create_user():
    payload = {
        "name": "John",
        "job": "QA Engineer"
    }

    response = requests.post(
        "https://reqres.in/api/users",
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 201, \
        f"Expected 201, got {response.status_code}"

    data = response.json()

    assert data["name"] == "John", \
        "Name doesn't match"

    assert data["job"] == "QA Engineer", \
        "Job doesn't match"

    print("PASS: test_create_user")


def test_update_user():
    payload = {
        "name": "John Updated",
        "job": "Senior QA"
    }

    response = requests.put(
        "https://reqres.in/api/users/2",
        headers=headers,
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}"

    data = response.json()

    assert data["name"] == "John Updated", \
        "Name doesn't match"

    assert data["job"] == "Senior QA", \
        "Job doesn't match"

    print("PASS: test_update_user")


test_get_users_list()
test_get_single_user()
test_get_non_existent_user()
test_create_user()
test_update_user()