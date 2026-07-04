from utils.config import (
    ADMIN_EMAIL,
    ADMIN_PASSWORD
)


def test_valid_login(client):

    payload = {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }

    response = client.post(
        "/auth/login",
        payload
    )

    assert response.status_code == 200

    assert "access_token" in response.json()


def test_invalid_login(client):

    payload = {
        "email": ADMIN_EMAIL,
        "password": "wrongpassword"
    }

    response = client.post(
        "/auth/login",
        payload
    )

    assert response.status_code == 401


def test_missing_password(client):

    payload = {
        "email": ADMIN_EMAIL
    }

    response = client.post(
        "/auth/login",
        payload
    )

    assert response.status_code in [400,422]