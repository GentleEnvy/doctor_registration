from src.db import db
from src.models import Patient, Doctor

__all__ = ['Appointment']


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record_time_id = db.Column(db.ForeignKey('record_time.id'))
    is_served = db.Column(db.Boolean, nullable=False, default=False)
    patient_id = db.Column(db.ForeignKey(Patient.id), nullable=False)
    doctor_id = db.Column(db.ForeignKey(Doctor.id), nullable=False)

    record_time = db.relationship('RecordTime', uselist=False)
    patient = db.relationship('Patient', uselist=False)
    doctor = db.relationship('Doctor', uselist=False)
