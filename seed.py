import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import random

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client[os.getenv("DB_NAME")]

async def seed():
    print("Seeding database...")

    # KPIs
    await db.kpis.drop()
    await db.kpis.insert_many([
        {"label": "Total Revenue",   "value": "$284,390", "change": 12.5,  "icon": "attach_money"},
        {"label": "Total Orders",    "value": "8,492",    "change": 8.3,   "icon": "shopping_cart"},
        {"label": "New Customers",   "value": "1,847",    "change": -3.1,  "icon": "person_add"},
        {"label": "Avg Order Value", "value": "$33.49",   "change": 4.7,   "icon": "trending_up"},
    ])
    print("✅ KPIs seeded")

    # Trends (90 days)
    await db.trends.drop()
    trends = []
    for i in range(90):
        d = datetime.now() - timedelta(days=89 - i)
        trends.append({
            "index":   i,
            "date":    d.strftime("%b %#d"),
            "revenue": round(5000 + random.random() * 10000, 2),
            "orders":  int(80 + random.random() * 200),
        })
    await db.trends.insert_many(trends)
    print("✅ Trends seeded")

    # Products
    await db.products.drop()
    await db.products.insert_many([
        {"rank": 1, "name": "Pro Wireless Headphones", "category": "Electronics", "revenue": 48200, "units": 964,  "trend": 18.2},
        {"rank": 2, "name": "Ergonomic Office Chair",  "category": "Furniture",   "revenue": 39800, "units": 312,  "trend": 7.4},
        {"rank": 3, "name": "Running Shoes X500",      "category": "Footwear",    "revenue": 32100, "units": 1423, "trend": 12.9},
        {"rank": 4, "name": "Smart Watch Series 4",    "category": "Electronics", "revenue": 28900, "units": 289,  "trend": -4.2},
        {"rank": 5, "name": "Organic Coffee Blend",    "category": "Food",        "revenue": 19400, "units": 4850, "trend": 22.7},
        {"rank": 6, "name": "Yoga Mat Pro",            "category": "Sports",      "revenue": 14200, "units": 947,  "trend": 31.1},
    ])
    print("✅ Products seeded")

    # Funnel
    await db.funnel.drop()
    await db.funnel.insert_many([
        {"stage": "Site Visitors",      "count": 24000, "percentage": 100},
        {"stage": "Product Page Views", "count": 14400, "percentage": 60},
        {"stage": "Add to Cart",        "count": 5760,  "percentage": 24},
        {"stage": "Checkout Started",   "count": 2880,  "percentage": 12},
        {"stage": "Purchase Completed", "count": 1584,  "percentage": 7},
    ])
    print("✅ Funnel seeded")

    # Categories
    await db.categories.drop()
    await db.categories.insert_many([
        {"category": "Electronics", "revenue": 112000},
        {"category": "Furniture",   "revenue":  78000},
        {"category": "Footwear",    "revenue":  54000},
        {"category": "Food",        "revenue":  36000},
        {"category": "Sports",      "revenue":  24000},
    ])
    print("✅ Categories seeded")

    print("\n🎉 Database seeded successfully!")
    client.close()

asyncio.run(seed())