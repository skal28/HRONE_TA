from fastapi import APIRouter, Depends, HTTPException, Query
from app.schemas.product import ProductCreate, ProductOut
from app.db.mongodb import get_db
from bson import ObjectId
from typing import List, Optional

router = APIRouter()

@router.post("/", response_model=ProductOut, status_code=201)
async def create_product(product: ProductCreate, db=Depends(get_db)):
    product_dict = product.dict()
    result = await db.products.insert_one(product_dict)
    product_dict["id"] = str(result.inserted_id)
    return product_dict

@router.get("/", response_model=List[ProductOut])
async def list_products(name: Optional[str] = None, size: Optional[str] = None, limit: int = 10, offset: int = 0, db=Depends(get_db)):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size
    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        product["id"] = str(product["_id"])
        products.append(product)
    return products