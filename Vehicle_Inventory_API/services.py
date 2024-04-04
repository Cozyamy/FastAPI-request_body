from typing import List, Union
from models import Vehicle

vehicles_db = [
    Vehicle(id=1, make='Toyota', model='Camry', price=25000000),
    Vehicle(id=2, make='Honda', model='Civic', price=22000000),
    Vehicle(id=3, make='Ford', model='F-150', price=3500000),
    Vehicle(id=4, make='Chevrolet', model='Silverado', price=40000000),
]

def get_vehicle_by_id(vehicle_id: int) -> Union[Vehicle, None]: #pragma: no cover
    for vehicle in vehicles_db:
        if vehicle.id == vehicle_id:
            return vehicle
    return None

def get_vehicles(make: str = None, model: str = None, price_range: str = None) -> Union[List[Vehicle], dict]: #pragma: no cover
    vehicles = vehicles_db

    if not any([make, model, price_range]):
        return vehicles

    filtered_vehicles = []
    for vehicle in vehicles:
        if model and model.lower() not in vehicle.model.lower():
            continue
        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            if not min_price <= vehicle.price <= max_price:
                continue
        if make and make.lower() != vehicle.make.lower():
            continue
        filtered_vehicles.append(vehicle)

    if not filtered_vehicles:
        return {"error": "No vehicle found that fits the provided parameters"}

    return filtered_vehicles