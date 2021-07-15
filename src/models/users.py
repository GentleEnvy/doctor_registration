from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.db import db

__all__ = ['User', 'Patient', 'Doctor', 'Admin']


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    mid_name = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    @property
    def patient(self):
        return Patient.query.filter_by(id=self.id).first()

    @property
    def doctor(self):
        return Doctor.query.filter_by(id=self.id).first()

    @property
    def admin(self):
        return Admin.query.filter_by(id=self.id).first()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Patient(User):
    id = db.Column(db.ForeignKey('user.id'), primary_key=True)

    appointment_set = db.relationship(
        'Appointment', uselist=True, back_populates='patient'
    )


class Doctor(User):
    id = db.Column(db.ForeignKey('user.id'), primary_key=True)
    specialty_id = db.Column(db.ForeignKey('specialty.id'))

    specialty = db.relationship('Specialty', uselist=False)
    record_times = db.relationship('RecordTime', uselist=True, back_populates='doctor')


class Admin(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
