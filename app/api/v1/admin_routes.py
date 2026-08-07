from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.permissions import admin_required
from app.database.database import get_db
from app.services.admin_service import get_all_users
from app.services.admin_service import get_all_donor_profiles
from app.services.admin_service import get_all_blood_requests_admin
router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def dashboard(current_user=Depends(admin_required)):
    return {
        "success": True,
        "message": "Welcome Admin",
        "data": current_user
    }
@router.get("/users")
def users(
    current_user=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return get_all_users(db)
@router.get("/donors")
def donors(
    current_user=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return get_all_donor_profiles(db)
@router.get("/blood-requests")
def blood_requests(
    current_user=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return get_all_blood_requests_admin(db)