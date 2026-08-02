from fastapi import APIRouter, Depends

from app.core.permissions import admin_required

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def dashboard(current_user=Depends(admin_required)):
    return {
        "success": True,
        "message": "Welcome Admin",
        "data": current_user
    }