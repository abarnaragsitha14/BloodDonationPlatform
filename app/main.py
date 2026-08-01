from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User
from app.api.v1.user_routes import router as user_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blood Donation Network & Emergency Matching Platform",
    version="1.0.0",
    description="REST API for Blood Donation Platform"
)

# Register API routes
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to Blood Donation Network API",
        "data": None
    }