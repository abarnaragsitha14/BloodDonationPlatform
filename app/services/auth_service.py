from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.core.jwt_handler import create_access_token

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def login_user(email: str, password: str, db: Session):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "detail": "Invalid Email"
        }

    if not pwd_context.verify(
        password,
        user.password
    ):
        return {
            "detail": "Invalid Password"
        }

    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }