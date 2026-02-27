from pydantic import BaseModel
from typing import Optional

class KpiCard(BaseModel):
    label: str
    value: str
    change: float
    icon: str

class SalesTrend(BaseModel):
    date: str
    revenue: float
    orders: int

class TopProduct(BaseModel):
    rank: int
    name: str
    category: str
    revenue: float
    units: int
    trend: float

class FunnelStage(BaseModel):
    stage: str
    count: int
    percentage: float