from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/categories")
async def get_categories():
    return await db.categories.find(
        {}, {"_id": 0}
    ).sort("revenue", -1).to_list(100)