from pydantic import BaseModel


class DoctorCreate(BaseModel):
    name: str


class PatientCreate(BaseModel):
    name: str
