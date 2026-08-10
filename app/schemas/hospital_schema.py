from pydantic import BaseModel


class HospitalCreate(BaseModel):
    hospital_name: str
    phone: str
    city: str
    state: str
    address: str | None = None
class HospitalUpdate(BaseModel):
    hospital_name: str
    phone: str
    city: str
    state: str
    address: str | None = None