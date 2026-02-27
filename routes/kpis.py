
from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/kpis")
async def get_kpis():
    kpis = await db.kpis.find({}, {"_id": 0}).to_list(100)
    return kpis