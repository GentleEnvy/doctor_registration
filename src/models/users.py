from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.db import db

__all__ = ['User', 'Patient', 'Doctor', 'Admin']


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    mid_name = db.Column(db.String(100), nullable=True)
    passport = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    patient = db.relationship('Patient', uselist=False)
    doctor = db.relationship('Doctor', uselist=False)
    admin = db.relationship('Admin', uselist=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Patient(User, db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class Doctor(User, db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class Admin(User, db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
