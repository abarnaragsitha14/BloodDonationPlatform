from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    hospital_name = Column(String(100), nullable=False)

    phone = Column(String(15), nullable=False)

    city = Column(String(100), nullable=False)

    state = Column(String(100), nullable=False)

    address = Column(String(255), nullable=True)

    user = relationship("User")