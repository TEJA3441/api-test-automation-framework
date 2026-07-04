from utils.data_generator import generate_user


def test_create_user(
        client,
        auth_token
):

    user = generate_user()

    headers = {
        "Authorization":
        f"Bearer {auth_token}"
    }

    response = client.post(
        "/users",
        user,
        headers
    )

    assert response.status_code == 201

    assert response.json()["email"] == user["email"]


def test_get_users(
        client,
        auth_token
):

    headers = {
        "Authorization":
        f"Bearer {auth_token}"
    }

    response = client.get(
        "/users",
        headers
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )