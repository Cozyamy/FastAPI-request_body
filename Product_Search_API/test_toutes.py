from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_product():
    response = client.get("/api/products?product_name=egg&price_range=10.0-40.0&category=food")
    assert response.status_code == 200
    data = response.json()
    assert data["products"] != []

def test_search_product_no_results():
    response = client.get("/api/products?product_name=nonexistent&price_range=10.0-40.0&category=food")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "No products found"

def test_search_product_with_price_range():
    response = client.get("/api/products?product_name=egg&price_range=20.0-30.0&category=food")
    assert response.status_code == 404


def test_search_product_without_category():
    response = client.get("/api/products?product_name=egg&price_range=10.0-40.0")
    assert response.status_code == 200
    data = response.json()
    assert data["products"] != []

def test_search_product_without_product_name():
    response = client.get("/api/products?price_range=10.0-40.0&category=food")
    assert response.status_code == 200
    data = response.json()
    assert data["products"] != []

def test_search_product_without_price_range():
    response = client.get("/api/products?product_name=egg&category=food")
    assert response.status_code == 200
    data = response.json()
    assert data["products"] != []