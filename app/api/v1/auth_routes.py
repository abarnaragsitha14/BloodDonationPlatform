from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.database.database import get_db
from app.services.auth_service import login_user

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        form_data.username,
        form_data.password,
        db
    )
@router.get("/me")
def get_current_user_details(
    current_user=Depends(get_current_user)
):
    return {
        "success": True,
        "message": "Current user fetched successfully",
        "data": {
            "id": current_user.id,
            "email": current_user.email,
            "role": current_user.role
        }
    }