from src.db import db

__all__ = ['Patient', 'Doctor', 'Admin']


class BaseUser:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__} ({self.username})>'


class Patient(BaseUser, db.Model):
    pass


class Doctor(BaseUser, db.Model):
    pass


class Admin(BaseUser, db.Model):
    pass
