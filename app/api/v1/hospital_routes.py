from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.permissions import hospital_required

from app.schemas.hospital_schema import HospitalCreate
from app.schemas.hospital_schema import HospitalUpdate
from app.services.hospital_service import create_hospital
from app.services.hospital_service import get_my_hospital
from app.services.hospital_service import update_my_hospital

router = APIRouter(
    prefix="/api/v1/hospitals",
    tags=["Hospitals"]
)


@router.post("/")
def create(
    hospital: HospitalCreate,
    current_user=Depends(hospital_required),
    db: Session = Depends(get_db)
):
    return create_hospital(
        hospital,
        current_user.id,
        db
    )
@router.get("/me")
def get_my_profile(
    current_user=Depends(hospital_required),
    db: Session = Depends(get_db)
):
    return get_my_hospital(
        current_user.id,
        db
    )
@router.put("/me")
def update_my_profile(
    hospital: HospitalUpdate,
    current_user=Depends(hospital_required),
    db: Session = Depends(get_db)
):
    return update_my_hospital(
        hospital,
        current_user.id,
        db
    )