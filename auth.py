from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(data: dict):
    if data["username"] == "admin" and data["password"] == "123":
        return {"token": "success"}
    return {"error": "invalid"}
🟦 doctor.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter()

@router.post("/")
def add_doctor(data: dict, db: Session = Depends(get_db)):
    d = models.Doctor(name=data["name"])
    db.add(d)
    db.commit()
    return d

@router.get("/")
def get_doctors(db: Session = Depends(get_db)):
    return db.query(models.Doctor).all()
