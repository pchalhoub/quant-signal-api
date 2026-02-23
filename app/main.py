from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Quant Signal API")

app.include_router(router)