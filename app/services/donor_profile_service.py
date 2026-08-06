from sqlalchemy.orm import Session

from app.models.user import User
from app.models.donor_profile import DonorProfile


def create_profile(profile_data, current_user, db: Session):

    user = db.query(User).filter(
        User.email == current_user["email"]
    ).first()

    existing = db.query(DonorProfile).filter(
        DonorProfile.user_id == user.id
    ).first()

    if existing:
        return {
            "success": False,
            "message": "Profile already exists",
            "data": None
        }

    profile = DonorProfile(
        user_id=user.id,
        blood_group=profile_data.blood_group,
        age=profile_data.age,
        gender=profile_data.gender,
        weight=profile_data.weight,
        city=profile_data.city,
        state=profile_data.state,
        phone=profile_data.phone,
        last_donation_date=profile_data.last_donation_date
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return {
        "success": True,
        "message": "Donor profile created successfully",
        "data": {
            "profile_id": profile.id
        }
    }
def get_profile(current_user, db):

    user = db.query(User).filter(
        User.email == current_user["email"]
    ).first()

    if not user:
        return {
            "success": False,
            "message": "User not found",
            "data": None
        }

    profile = db.query(DonorProfile).filter(
        DonorProfile.user_id == user.id
    ).first()

    if not profile:
        return {
            "success": False,
            "message": "Donor profile not found",
            "data": None
        }

    return {
        "success": True,
        "message": "Donor profile fetched successfully",
        "data": {
            "blood_group": profile.blood_group,
            "age": profile.age,
            "gender": profile.gender,
            "weight": profile.weight,
            "phone": profile.phone,
            "city": profile.city,
            "state": profile.state,
            "last_donation_date": profile.last_donation_date,
            "availability": profile.availability
        }
    }
def update_donor_profile(profile_data, user_id, db):
    profile = db.query(DonorProfile).filter(
        DonorProfile.user_id == user_id
    ).first()

    if not profile:
        return {
            "success": False,
            "message": "Profile not found",
            "data": None
        }

    profile.blood_group = profile_data.blood_group
    profile.age = profile_data.age
    profile.gender = profile_data.gender
    profile.weight = profile_data.weight
    profile.city = profile_data.city
    profile.state = profile_data.state
    profile.last_donation_date = profile_data.last_donation_date
    profile.availability = profile_data.availability

    db.commit()
    db.refresh(profile)

    return {
        "success": True,
        "message": "Profile updated successfully",
        "data": profile
    }