from src.db import db

__all__ = ['RecordTime']


class RecordTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.ForeignKey('doctor.id'))
    weekday = db.Column(db.Integer, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

    doctor = db.relationship('Doctor', uselist=False, back_populates='record_times')
    appointment = db.relationship(
        'Appointment', uselist=False, back_populates='record_time'
    )
