from models import Product
from typing import List

products_db = [
    Product(name="egg", category="food", price=10.0),
    Product(name="Product 2", category="Category 2", price=20.0),
    Product(name="Product 3", category="Category 1", price=30.0),
    Product(name="Product 4", category="Category 2", price=40.0),
]

def filter_products(product_name: str, price_range: str, category: str) -> dict:
    filtered_products = []

    for product in products_db:
        if product_name and product_name.lower() not in product.name.lower():
            continue
        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            if not (min_price <= product.price <= max_price):
                continue
        if category and category.lower() != product.category.lower():
            continue
        filtered_products.append(product)

    if not filtered_products:
        return {"products": []}
    
    return {"products": filtered_products}