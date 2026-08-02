from fastapi import APIRouter, Depends

from app.core.security import get_current_user

router = APIRouter(
    prefix="/api/v1/profile",
    tags=["Profile"]
)


@router.get("/")
def profile(current_user=Depends(get_current_user)):
    return {
        "success": True,
        "message": "Profile fetched successfully",
        "data": current_user
    }