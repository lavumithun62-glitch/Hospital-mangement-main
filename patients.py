from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter()

@router.post("/")
def add_patient(data: dict, db: Session = Depends(get_db)):
    p = models.Patient(name=data["name"])
    db.add(p)
    db.commit()
    return p

@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()
