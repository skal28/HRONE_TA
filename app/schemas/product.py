from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    size: Optional[str] = None
    tags: Optional[List[str]] = []

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: str