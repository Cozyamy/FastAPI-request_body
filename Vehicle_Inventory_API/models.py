from pydantic import BaseModel

class Vehicle(BaseModel):
    id: int
    make: str
    model: str
    price: int