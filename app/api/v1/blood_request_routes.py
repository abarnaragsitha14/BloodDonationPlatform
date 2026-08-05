from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.blood_request_schema import BloodRequestCreate
from app.services.blood_request_service import create_blood_request

router = APIRouter(
    prefix="/api/v1/blood-request",
    tags=["Blood Request"]
)


@router.post("/")
def create_request(
    request: BloodRequestCreate,
    db: Session = Depends(get_db)
):
    return create_blood_request(
        request,
        db
    )