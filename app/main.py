from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.models.user import User
from app.models.donor_profile import DonorProfile
from app.models.hospital import Hospital
from app.api.v1.user_routes import router as user_router
from app.api.v1.auth_routes import router as auth_router
from app.api.v1.profile_routes import router as profile_router
from app.api.v1.admin_routes import router as admin_router
from app.api.v1.blood_request_routes import router as blood_request_router
from app.api.v1.matching_routes import router as matching_router
from app.api.v1.donor_profile_routes import router as donor_profile_router
from app.api.v1.notification_routes import router as notification_router
from app.api.v1.hospital_routes import router as hospital_router
from app.models.blood_request import BloodRequest 
from app.models.notifications import Notification
# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blood Donation Network & Emergency Matching Platform",
    version="1.0.0",
    description="REST API for Blood Donation Platform"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(admin_router)
app.include_router(donor_profile_router)
app.include_router(blood_request_router)
app.include_router(matching_router)
app.include_router(notification_router)
app.include_router(hospital_router)



@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to Blood Donation Network API",
        "data": None
    }