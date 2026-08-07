from app.models.user import User


def get_all_users(db):

    users = db.query(User).all()

    return {
        "success": True,
        "message": "Users fetched successfully",
        "data": [
            {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role
            }
            for user in users
        ]
    }