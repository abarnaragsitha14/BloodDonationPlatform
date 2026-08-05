from sqlalchemy.orm import Session

from app.models.blood_request import BloodRequest
from app.models.donor_profile import DonorProfile


def find_matching_donors(request_id: int, db: Session):

    request = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not request:
        return {
            "success": False,
            "message": "Blood request not found",
            "data": None
        }

    donors = db.query(DonorProfile).filter(
        DonorProfile.blood_group == request.blood_group,
        DonorProfile.city == request.city,
        DonorProfile.availability == "Available"
    ).all()

    result = []

    for donor in donors:
        result.append({
            "id": donor.id,
            "blood_group": donor.blood_group,
            "city": donor.city,
            "phone": donor.phone
        })

    return {
        "success": True,
        "message": "Matching donors found",
        "data": result
    }