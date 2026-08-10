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
def get_user_notifications(user_id: int, db: Session):

    notifications = db.query(Notification).filter(
        Notification.user_id == user_id
    ).all()

    return {
        "success": True,
        "message": "Notifications fetched successfully",
        "data": [
            {
                "id": notification.id,
                "title": notification.title,
                "message": notification.message,
                "status": notification.status
            }
            for notification in notifications
        ]
    }
def mark_notification_as_read(
    notification_id: int,
    user_id: int,
    db: Session
):

    notification = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == user_id
    ).first()

    if notification is None:
        return {
            "success": False,
            "message": "Notification not found",
            "data": None
        }

    notification.status = "Read"

    db.commit()
    db.refresh(notification)

    return {
        "success": True,
        "message": "Notification marked as read",
        "data": {
            "id": notification.id,
            "title": notification.title,
            "message": notification.message,
            "status": notification.status
        }
    }