from fastapi import FastAPI
from routes import router as product_router
from routes import router

app = FastAPI()

app.include_router(product_router)