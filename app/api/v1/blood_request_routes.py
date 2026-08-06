from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.blood_request_schema import BloodRequestCreate
from app.services.blood_request_service import create_blood_request
from app.services.blood_request_service import get_all_blood_requests
from app.services.blood_request_service import get_blood_request_by_id
from app.services.blood_request_service import update_blood_request
from app.services.blood_request_service import  delete_blood_request
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
@router.get("/")
def get_requests(
    db: Session = Depends(get_db)
):
    return get_all_blood_requests(db)
@router.get("/{request_id}")
def get_request(
    request_id: int,
    db: Session = Depends(get_db)
):
    return get_blood_request_by_id(
        request_id,
        db
    )
@router.put("/{request_id}")
def update_request(
    request_id: int,
    request: BloodRequestCreate,
    db: Session = Depends(get_db)
):
    return update_blood_request(
        request_id,
        request,
        db
    )
@router.delete("/{request_id}")
def delete_request(
    request_id: int,
    db: Session = Depends(get_db)
):
    return delete_blood_request(
        request_id,
        db
    )