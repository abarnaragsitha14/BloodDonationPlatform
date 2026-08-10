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
def get_blood_request_by_id(request_id: int, db):

    request = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not request:
        return {
            "success": False,
            "message": "Blood request not found",
            "data": None
        }

    return {
        "success": True,
        "message": "Blood request fetched successfully",
        "data": {
            "id": request.id,
            "patient_name": request.patient_name,
            "blood_group": request.blood_group,
            "units_required": request.units_required,
            "hospital_name": request.hospital_name,
            "city": request.city,
            "state": request.state,
            "emergency_level": request.emergency_level,
            "status": request.status
        }
    }
def update_blood_request(request_id: int, request_data, db):

    request = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not request:
        return {
            "success": False,
            "message": "Blood request not found",
            "data": None
        }

    request.patient_name = request_data.patient_name
    request.blood_group = request_data.blood_group
    request.units_required = request_data.units_required
    request.hospital_name = request_data.hospital_name
    request.city = request_data.city
    request.state = request_data.state
    request.contact_number = request_data.contact_number
    request.emergency_level = request_data.emergency_level

    db.commit()
    db.refresh(request)

    return {
        "success": True,
        "message": "Blood request updated successfully",
        "data": {
            "id": request.id,
            "patient_name": request.patient_name,
            "blood_group": request.blood_group
        }
    }
def delete_blood_request(request_id: int, db):

    request = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not request:
        return {
            "success": False,
            "message": "Blood request not found",
            "data": None
        }

    db.delete(request)
    db.commit()

    return {
        "success": True,
        "message": "Blood request deleted successfully",
        "data": None
    }
def update_request_status(
    request_id: int,
    status: str,
    db: Session
):

    request = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not request:
        return {
            "success": False,
            "message": "Blood request not found",
            "data": None
        }

    allowed_statuses = [
        "Pending",
        "Matching",
        "Fulfilled",
        "Cancelled"
    ]

    if status not in allowed_statuses:
        return {
            "success": False,
            "message": "Invalid request status",
            "data": None
        }

    request.status = status

    db.commit()
    db.refresh(request)

    return {
        "success": True,
        "message": "Blood request status updated successfully",
        "data": {
            "id": request.id,
            "status": request.status
        }
    }
