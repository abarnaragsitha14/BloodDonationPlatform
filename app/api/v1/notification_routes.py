from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.notification_service import create_notification

router = APIRouter(
    prefix="/api/v1/notifications",
    tags=["Notifications"]
)


@router.post("/")
def create(
    user_id: int,
    title: str,
    message: str,
    db: Session = Depends(get_db)
):
    return create_notification(
        user_id,
        title,
        message,
        db
    )