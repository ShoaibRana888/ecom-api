from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import kpis, trends, products, funnel, categories

app = FastAPI(title="EcomAnalytics API")

# CORS — allow Angular dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ecom-analytics-ten.vercel.app/",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(kpis.router,     prefix="/api")
app.include_router(trends.router,   prefix="/api")
app.include_router(products.router, prefix="/api")
app.include_router(funnel.router,   prefix="/api")
app.include_router(categories.router,  prefix="/api")

@app.get("/")
def root():
    return {"status": "ok"}