from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True, index=True)

    patient_name = Column(String(100), nullable=False)
    blood_group = Column(String(5), nullable=False)
    units_required = Column(Integer, nullable=False)

    hospital_name = Column(String(100), nullable=False)

    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)

    contact_number = Column(String(15), nullable=False)

    emergency_level = Column(String(20), nullable="True")

    status = Column(String(20), default="Pending")

    created_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship("User")