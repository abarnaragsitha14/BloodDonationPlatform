from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import get_current_user

from app.schemas.hospital_schema import HospitalCreate
from app.services.hospital_service import create_hospital


router = APIRouter(
    prefix="/api/v1/hospitals",
    tags=["Hospitals"]
)


@router.post("/")
def create(
    hospital: HospitalCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_hospital(
        hospital,
        current_user.id,
        db
    )