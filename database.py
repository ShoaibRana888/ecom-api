import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("MONGODB_URL")

client = AsyncIOMotorClient(
    url,
    tls=True,
    tlsAllowInvalidCertificates=True
)
db = client[os.getenv("DB_NAME")]