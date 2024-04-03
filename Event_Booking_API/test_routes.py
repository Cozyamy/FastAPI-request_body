from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)

def test_book_event():
    booking_data = {
        "attendee": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 25
        },
        "event": {
            "name": "Concert",
            "date": "2024-04-02",
            "location": "Venue A"
        },
        "ticket_type": "VIP"
    }
    response = client.post("/booking/book_event", json=booking_data)
    assert response.status_code == 201
    
    data = response.json()
    assert "data" in data
    assert "attendee" in data["data"]
    assert data["data"]["attendee"]["name"] == "John Doe"
    assert "event" in data["data"]
    assert data["data"]["event"]["name"] == "Concert"
    assert "ticket_type" in data["data"]
    assert data["data"]["ticket_type"] == "VIP"

def test_book_event_error_handling():
    booking_data = {
        "attendee": {
            "name": "John Doe",
            "email": "john@example.com",
            "age": "invalid"
        },
        "event": {
            "name": "Concert",
            "date": "2024-04-02",
            "location": "Venue A"
        },
        "ticket_type": "VIP"
    }
    response = client.post("/booking/book_event", json=booking_data)
    assert response.status_code == 422

