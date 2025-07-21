from fastapi import FastAPI
from app.routers import products, orders
from app.db.mongodb import connect_db

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_db()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])