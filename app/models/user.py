from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.database.database import Base
from app.utils.roles import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, index=True, nullable=False)

    phone = Column(String(15), unique=True, nullable=True)

    password = Column(String(255), nullable=False)

    role = Column(
        Enum(
            UserRole,
            values_callable=lambda enum: [e.value for e in enum]
        ),
        default=UserRole.DONOR.value,
        nullable=False
    )

    is_active = Column(Boolean, default=True)