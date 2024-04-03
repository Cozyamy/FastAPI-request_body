from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    category: str
    price: float

class ProductResponse(BaseModel):
    products: List[Product]