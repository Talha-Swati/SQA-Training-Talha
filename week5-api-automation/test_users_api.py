import pytest
import json

from api_helpers import get_user, update_user, create_user


# Test 1: Parameterized GET user testing
@pytest.mark.parametrize("user_id, expected_status", [
    (2, 200),
    (999, 404),
    (23, 404)
])
def test_get_user_status(user_id, expected_status):

    response = get_user(user_id)

    if response.status_code != expected_status:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
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

    response = update_user(user_id, payload)

    if response.status_code != 200:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
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

    response = create_user(user)

    if response.status_code != 201:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == user["name"]
    assert data["job"] == user["job"]

    assert "id" in data
    assert "createdAt" in data