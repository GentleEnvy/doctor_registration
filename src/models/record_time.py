from src.db import db

__all__ = ['RecordTime']


class RecordTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.ForeignKey('doctor.id'))
    weekday = db.Column(db.Integer, nullable=False)
    start = db.Column(db.Time, nullable=False)
    end = db.Column(db.Time, nullable=False)

    doctor = db.relationship('Doctor', uselist=False, back_populates='record_times')
    appointment_set = db.relationship(
        'Appointment', uselist=True, back_populates='record_time'
    )

    def get_appointment(self, date):
        for appointment in self.appointment_set:
            if appointment.date == date:
                return appointment
        return None
