import pytest

from utils.api_client import APIClient
from utils.config import (
    BASE_URL,
    ADMIN_EMAIL,
    ADMIN_PASSWORD
)


@pytest.fixture(scope="session")
def client():

    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(client):

    payload = {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }

    response = client.post(
        "/auth/login",
        payload
    )

    token = response.json()["access_token"]

    return token