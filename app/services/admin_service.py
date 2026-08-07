from app.models.user import User
from app.models.donor_profile import DonorProfile
from app.models.blood_request import BloodRequest

def get_all_users(db):

    users = db.query(User).all()

    return {
        "success": True,
        "message": "Users fetched successfully",
        "data": [
            {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role
            }
            for user in users
        ]
    }
def get_all_donor_profiles(db):

    donors = db.query(DonorProfile).all()

    return {
        "success": True,
        "message": "Donor profiles fetched successfully",
        "data": [
            {
                "id": donor.id,
                "user_id": donor.user_id,
                "blood_group": donor.blood_group,
                "age": donor.age,
                "gender": donor.gender,
                "weight": donor.weight,
                "city": donor.city,
                "state": donor.state,
                "phone": donor.phone,
                "last_donation_date": donor.last_donation_date,
                "availability": donor.availability
            }
            for donor in donors
        ]
    }
def get_all_blood_requests_admin(db):

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
                "contact_number": request.contact_number,
                "status": request.status,
                "emergency_level": request.emergency_level
            }
            for request in requests
        ]
    }