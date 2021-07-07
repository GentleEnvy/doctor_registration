from src.db import db
from src.models import Patient, Doctor

__all__ = ['Appointment']


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, unique=True)
    patient_id = db.Column(db.ForeignKey(Patient.id), nullable=False)
    doctor_id = db.Column(db.ForeignKey(Doctor.id), nullable=False)
