from sqlalchemy.orm import Session

from app.models.blood_request import BloodRequest


def create_blood_request(request_data, db: Session):

    request = BloodRequest(
        patient_name=request_data.patient_name,
        blood_group=request_data.blood_group,
        units_required=request_data.units_required,
        hospital_name=request_data.hospital_name,
        city=request_data.city,
        state=request_data.state,
        contact_number=request_data.contact_number,
        emergency_level="Medium"
    )

    db.add(request)
    db.commit()
    db.refresh(request)

    return {
        "success": True,
        "message": "Blood request created successfully",
        "data": {
            "id": request.id,
            "patient_name": request.patient_name,
            "blood_group": request.blood_group,
            "city": request.city
        }
    }
def get_all_blood_requests(db):

    requests = db.query(BloodRequest).all()

    return {
        "success": True,
        "message": "Blood requests fetched successfully",
        "data": [
            {
                "id": request.id,
                "patient_name": request.patient_name,
                "blood_group": request.blood_group,
                "units_required": request.units_required,
                "hospital_name": request.hospital_name,
                "city": request.city,
                "state": request.state,
                "emergency_level": request.emergency_level
            }
            for request in requests
        ]
    }