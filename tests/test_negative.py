def test_invalid_user_id(
        client,
        auth_token
):

    headers = {
        "Authorization":
        f"Bearer {auth_token}"
    }

    response = client.get(
        "/users/999999",
        headers
    )

    assert response.status_code == 404


def test_empty_user_creation(
        client,
        auth_token
):

    headers = {
        "Authorization":
        f"Bearer {auth_token}"
    }

    response = client.post(
        "/users",
        {},
        headers
    )

    assert response.status_code == 422