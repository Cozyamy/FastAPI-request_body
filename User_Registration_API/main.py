from fastapi import FastAPI
from routes import router
from config import create_file 

app = FastAPI()

create_file()

app.include_router(router, prefix='/v1')
