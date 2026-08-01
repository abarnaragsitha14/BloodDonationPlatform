from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user_schema import UserCreate
from app.services.user_service import register_user

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)