import requests
from config import BASE_URL, HEADERS, TIMEOUT


def get_users():
    return requests.get(
        f"{BASE_URL}/users",
        headers=HEADERS,
        timeout=TIMEOUT
    )


def get_user(user_id):
    return requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers=HEADERS,
        timeout=TIMEOUT
    )


def create_user(payload):
    return requests.post(
        f"{BASE_URL}/users",
        json=payload,
        headers=HEADERS,
        timeout=TIMEOUT
    )


def update_user(user_id, payload):
    return requests.put(
        f"{BASE_URL}/users/{user_id}",
        json=payload,
        headers=HEADERS,
        timeout=TIMEOUT
    )


def delete_user(user_id):
    return requests.delete(
        f"{BASE_URL}/users/{user_id}",
        headers=HEADERS,
        timeout=TIMEOUT
    )


def login(email, password=None):
    body = {
        "email": email
    }

    if password is not None:
        body["password"] = password

    return requests.post(
        f"{BASE_URL}/login",
        json=body,
        headers=HEADERS,
        timeout=TIMEOUT
    )