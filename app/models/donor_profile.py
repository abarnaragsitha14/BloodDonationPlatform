from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class DonorProfile(Base):
    __tablename__ = "donor_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    blood_group = Column(String(5), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    weight = Column(Integer, nullable=False)
    phone = Column(String(15),nullable=False)

    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)

    last_donation_date = Column(String(20), nullable=True)

    availability = Column(String(20), default="Available")

    user = relationship("User")