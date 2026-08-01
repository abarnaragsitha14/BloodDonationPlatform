from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user_schema import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def register_user(user: UserCreate, db: Session):

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered",
            "data": None
        }

    # Hash password
    hashed_password = pwd_context.hash(user.password)

    # Create new user
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hashed_password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "success": True,
        "message": "User registered successfully",
        "data": new_user
    }