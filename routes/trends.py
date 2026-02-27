from fastapi import APIRouter, Query
from database import db

router = APIRouter()

@router.get("/trends")
async def get_trends(days: int = Query(default=30)):
    trends = await db.trends.find(
        {}, {"_id": 0}
    ).sort("date", -1).limit(days).to_list(days)
    return list(reversed(trends))