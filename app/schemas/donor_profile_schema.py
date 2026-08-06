from pydantic import BaseModel


class DonorProfileCreate(BaseModel):
    blood_group: str
    age: int
    gender: str
    weight: int
    city: str
    state: str
    phone: str
    last_donation_date: str | None = None
    availability: str