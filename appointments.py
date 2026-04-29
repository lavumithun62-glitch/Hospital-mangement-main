from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter()

@router.post("/")
def book(data: dict, db: Session = Depends(get_db)):
    a = models.Appointment(
        doctor_id=data["doctor_id"],
        patient_id=data["patient_id"]
    )
    db.add(a)
    db.commit()
    return a
