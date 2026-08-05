from pydantic import BaseModel


class BloodRequestCreate(BaseModel):
    patient_name: str
    blood_group: str
    units_required: int
    hospital_name: str
    city: str
    state: str
    contact_number: str