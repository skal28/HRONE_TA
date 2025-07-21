from fastapi import APIRouter, Depends
from app.schemas.order import OrderCreate, OrderOut
from app.db.mongodb import get_db
from datetime import datetime
from bson import ObjectId
from typing import List

router = APIRouter()

@router.post("/", response_model=OrderOut, status_code=201)
async def create_order(order: OrderCreate, db=Depends(get_db)):
    order_dict = order.dict()
    order_dict["created_at"] = datetime.utcnow()
    result = await db.orders.insert_one(order_dict)
    order_dict["id"] = str(result.inserted_id)
    return order_dict

@router.get("/{user_id}", response_model=List[OrderOut])
async def list_orders(user_id: str, limit: int = 10, offset: int = 0, db=Depends(get_db)):
    cursor = db.orders.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        order["id"] = str(order["_id"])
        orders.append(order)
    return orders