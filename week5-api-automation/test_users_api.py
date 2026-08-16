import requests
import pytest
import json

BASE_URL = "https://reqres.in/api"
API_KEY = "free_user_3HX1rLoxrzgyA5WpxMc3rpqcUle"


headers = {
    "x-api-key": API_KEY
}


# Test 1: Parameterized GET user testing
@pytest.mark.parametrize("user_id, expected_status", [
    (2, 200),
    (999, 404),
    (23, 404)
])
def test_get_user_status(user_id, expected_status):
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers=headers
    )

    assert response.status_code == expected_status


# Test 2: Parameterized PUT update testing
@pytest.mark.parametrize("user_id, name, job", [
    (2, "John", "QA Engineer"),
    (3, "Ali", "Developer"),
    (4, "Sara", "Tester")
])
def test_update_user(user_id, name, job):

    payload = {
        "name": name,
        "job": job
    }

    response = requests.put(
        f"{BASE_URL}/users/{user_id}",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == name
    assert data["job"] == job


# Read POST test data from JSON file
with open("test_data.json", "r") as file:
    test_users = json.load(file)


# Test 3: POST users using JSON test data
@pytest.mark.parametrize("user", test_users)
def test_create_user(user):

    response = requests.post(
        f"{BASE_URL}/users",
        json=user,
        headers=headers
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == user["name"]
    assert data["job"] == user["job"]

    assert "id" in data
    assert "createdAt" in data