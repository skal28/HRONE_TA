from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderBase(BaseModel):
    user_id: str
    items: List[OrderItem]

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: str
    created_at: datetime