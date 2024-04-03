from fastapi.testclient import TestClient
from main import app


client = TestClient(app=app)


def test_successful_user_registration():
    response = client.post(
        "/v1/api/register",
        json={
            "username": "Unique User",
            "email": "unique@example.com",
            "password": "Welcome2$",
        },
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Successfully created"}


def test_user_exists():
    response = client.post(
        "/v1/api/register",
        json={
            "username": "Unique User",
            "email": "unique@example.com",
            "password": "Welcome2$",
        },
    )
    assert response.json() == {"error": "User already exists"}
    assert response.status_code == 409

def test_register_user_invalid_password():
    response = client.post(
        "/v1/api/register",
        json={
            "username": "West Lif",
            "email": "wlif@example.com",
            "password": "Welcome2",
        },
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "value_error",
                "loc": ["body", "password"],
                "msg": "Value error, Password does not meet stipulated criteria",
                "input": "Welcome2",
                "ctx": {"error": {}},
                "url": "https://errors.pydantic.dev/2.6/v/value_error",
            }
        ]
    }


def test_register_user_same_name():
    response = client.post(
        "/v1/api/register",
        json={
            "username": "Unique User",
            "email": "unique@example.com",
            "password": "Welcome2$",
        },
    )
    assert response.status_code == 409
    assert response.json() == {"error": "User already exists"}
