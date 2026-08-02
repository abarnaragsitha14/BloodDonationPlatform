from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.user import User
from app.models.donor_profile import DonorProfile
from app.api.v1.user_routes import router as user_router
from app.api.v1.auth_routes import router as auth_router
from app.api.v1.profile_routes import router as profile_router
from app.api.v1.admin_routes import router as admin_router
from app.api.v1.donor_profile_routes import router as donor_profile_router
# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blood Donation Network & Emergency Matching Platform",
    version="1.0.0",
    description="REST API for Blood Donation Platform"
)

# Register API routes
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(admin_router)
app.include_router(donor_profile_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to Blood Donation Network API",
        "data": None
    }