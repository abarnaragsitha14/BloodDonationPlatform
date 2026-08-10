from sqlalchemy.orm import Session

from app.models.notifications import Notification


def create_notification(
    user_id: int,
    title: str,
    message: str,
    db: Session
):

    notification = Notification(
        user_id=user_id,
        title=title,
        message=message
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return {
        "success": True,
        "message": "Notification created successfully",
        "data": {
            "id": notification.id,
            "title": notification.title,
            "message": notification.message,
            "status": notification.status
        }
    }