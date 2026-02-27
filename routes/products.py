from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/products")
async def get_products():
    products = await db.products.find(
        {}, {"_id": 0}
    ).sort("revenue", -1).to_list(100)
    return products