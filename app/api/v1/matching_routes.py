from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.matching_service import find_matching_donors

router = APIRouter(
    prefix="/api/v1/match",
    tags=["Emergency Matching"]
)


@router.get("/{request_id}")
def match_donors(
    request_id: int,
    db: Session = Depends(get_db)
):
    return find_matching_donors(
        request_id,
        db
    )