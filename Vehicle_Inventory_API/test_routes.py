from fastapi.testclient import TestClient
from main import app

client = TestClient(app=app)

def test_get_vehicle_by_id():
    response = client.get("/api/vehicles/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_get_vehicle_by_id_not_found():
    response = client.get("/api/vehicles/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_get_vehicle_by_params():
    response = client.get("/api/vehicles?make=Toyota&price_range=20000-30000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_get_vehicle_by_invalid_params():
    response = client.get("/api/vehicles?make=InvalidMake")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}