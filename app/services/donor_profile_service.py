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