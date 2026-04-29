from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import doctor, patient, appointment, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(auth.router)
app.include_router(doctor.router, prefix="/doctors")
app.include_router(patient.router, prefix="/patients")
app.include_router(appointment.router, prefix="/appointments")

