import pytest
import json

from api_helpers import (
    get_users,
    get_user,
    create_user,
    update_user,
    delete_user,
    login
)


# Read POST test data from JSON file
with open("test_data.json", "r") as file:
    test_users = json.load(file)


# Test 1: GET list of users
def test_get_users_list():

    response = get_users()

    if response.status_code != 200:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 200

    data = response.json()

    assert "data" in data
    assert len(data["data"]) > 0


# Test 2: GET single valid user
@pytest.mark.parametrize("user_id", [
    1,
    2
])
def test_get_single_valid_user(user_id):

    response = get_user(user_id)

    if response.status_code != 200:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["id"] == user_id


# Test 3: GET single invalid user
@pytest.mark.parametrize("user_id", [
    999,
    23
])
def test_get_single_invalid_user(user_id):

    response = get_user(user_id)

    if response.status_code != 404:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 404
    assert response.json() == {}


# Test 4: POST create user
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


# Test 5: PUT update user
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
    assert "updatedAt" in data


# Test 6: DELETE user
def test_delete_user():

    response = delete_user(2)

    if response.status_code != 204:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 204
    assert response.text == ""


# Test 7: POST login success
def test_login_success():

    response = login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    if response.status_code != 200:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert len(data["token"]) > 0


# Test 8: POST login missing password
def test_login_missing_password():

    response = login(
        "peter@klaven"
    )

    if response.status_code != 400:
        print(
            f"FAILED: {response.url} -> "
            f"{response.status_code} -> {response.text}"
        )

    assert response.status_code == 400

    data = response.json()

    assert "error" in data
    assert len(data["error"]) > 0