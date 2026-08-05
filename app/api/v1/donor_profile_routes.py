from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import get_current_user
from app.schemas.donor_profile_schema import DonorProfileCreate
from app.services.donor_profile_service import create_profile
from app.services.donor_profile_service import get_profile

router = APIRouter(
    prefix="/api/v1/donor",
    tags=["Donor Profile"]
)


@router.post("/profile")
def donor_profile(
    profile: DonorProfileCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_profile(
        profile,
        current_user,
        db
    )
@router.get("/")
def view_profile(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_profile(
        current_user,
        db
    )