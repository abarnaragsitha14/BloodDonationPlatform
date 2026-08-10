from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.database.database import get_db
from app.services.notification_service import create_notification
from app.services.notification_service import get_user_notifications
from app.services.notification_service import mark_notification_as_read
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
@router.get("/")
def get_notifications(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_user_notifications(
        current_user.id,
        db
    )
@router.put("/{notification_id}/read")
def mark_as_read(
    notification_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return mark_notification_as_read(
        notification_id,
        current_user.id,
        db
    )