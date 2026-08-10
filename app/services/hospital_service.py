from sqlalchemy.orm import Session

from app.models.hospital import Hospital
from app.schemas.hospital_schema import HospitalCreate


def create_hospital(
    hospital_data: HospitalCreate,
    user_id: int,
    db: Session
):

    existing_hospital = db.query(Hospital).filter(
        Hospital.user_id == user_id
    ).first()

    if existing_hospital:
        return {
            "success": False,
            "message": "Hospital profile already exists",
            "data": None
        }

    hospital = Hospital(
        user_id=user_id,
        hospital_name=hospital_data.hospital_name,
        phone=hospital_data.phone,
        city=hospital_data.city,
        state=hospital_data.state,
        address=hospital_data.address
    )

    db.add(hospital)
    db.commit()
    db.refresh(hospital)

    return {
        "success": True,
        "message": "Hospital profile created successfully",
        "data": {
            "id": hospital.id,
            "hospital_name": hospital.hospital_name,
            "phone": hospital.phone,
            "city": hospital.city,
            "state": hospital.state,
            "address": hospital.address
        }
    }
def get_my_hospital(
    user_id: int,
    db: Session
):
    hospital = db.query(Hospital).filter(
        Hospital.user_id == user_id
    ).first()

    if not hospital:
        return {
            "success": False,
            "message": "Hospital profile not found",
            "data": None
        }

    return {
        "success": True,
        "message": "Hospital profile fetched successfully",
        "data": {
            "id": hospital.id,
            "hospital_name": hospital.hospital_name,
            "phone": hospital.phone,
            "city": hospital.city,
            "state": hospital.state,
            "address": hospital.address
        }
    }