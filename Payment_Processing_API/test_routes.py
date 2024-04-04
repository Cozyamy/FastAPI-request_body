from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_make_payment_success():
    payment_data = {
        "amount": 1000,
        "card": {
            "name_on_card": "Fortune Okolo",
            "card_no": "4000122356789010",
            "cvv": "123",
            "expiry_date": "11/24"
            }
    }
    response = client.post("/payments", json=payment_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Transaction completed"}

def test_make_payment_failure_expired_card():
    expired_payment_data = {
        "amount": 1000,
        "card": {
            "name_on_card": "Fortune Okolo",
            "card_no": "4000122356789010",
            "cvv": "123",
            "expiry_date": "11/21"
            }
    }
    response = client.post("/payments", json=expired_payment_data)
    assert response.status_code == 422

def test_make_payment_failure_incorrect_cvv():
    incorrect_cvv_payment_data = {
        "amount": 1000,
        "card": {
            "name_on_card": "Fortune Okolo",
            "card_no": "4000122356789010",
            "cvv": "12345",
            "expiry_date": "11/24"
            }
    }
    response = client.post("/payments", json=incorrect_cvv_payment_data)
    assert response.status_code == 422

def test_make_payment_failure_short_name():
    short_name_payment_data = {
        "amount": 1000,
        "card": {
            "name_on_card": "Fo",
            "card_no": "4000122356789010",
            "cvv": "123",
            "expiry_date": "11/24"
            }
    }
    response = client.post("/payments", json=short_name_payment_data)
    assert response.status_code == 422



