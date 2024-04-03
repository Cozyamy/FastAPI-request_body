from fastapi import APIRouter, Query, HTTPException
from models import ProductResponse
from services import filter_products

router = APIRouter(prefix='/api', tags=["Filter Products"])

@router.get('/products', response_model=ProductResponse)
async def search_product(
    product_name: str = Query(default=None, description="Product Name"),
    price_range: str = Query(default=None, description="Price Range"),
    category: str = Query(default=None, description="Category")
) -> ProductResponse:
    filtered_products = filter_products(product_name, price_range, category)
    if not filtered_products["products"]:
        raise HTTPException(status_code=404, detail="No products found")
    return ProductResponse(**filtered_products)