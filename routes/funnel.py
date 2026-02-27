from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/funnel")
async def get_funnel():
    stages = await db.funnel.find({}, {"_id": 0}).to_list(100)
    return stages