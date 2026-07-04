import json
import pytest


with open(
    "test_data/login_data.json"
) as file:

    data = json.load(file)


@pytest.mark.parametrize(
    "payload",
    data
)
def test_login_data_driven(
        client,
        payload
):

    response = client.post(
        "/auth/login",
        {
            "email":
            payload["email"],

            "password":
            payload["password"]
        }
    )

    assert response.status_code == payload["status"]