from datetime import date as python_date

from werkzeug.utils import redirect
from flask_login import current_user

from src.db import db
from src.models import Appointment, Doctor, RecordTime
from src.urls.base import BaseUrl

__all__ = ['AppointmentUrl']


class AppointmentUrl(BaseUrl):
    url = '/signup/appointment'

    def get(self, request):
        date = request.args['date']
        doctor_id = request.args['doctor']
        appointment = Appointment(
            record_time_id=RecordTime.query.filter_by(
                doctor_id=Doctor.query.filter_by(id=doctor_id).first().id,
                weekday=python_date.fromisoformat(date).weekday()
            ).first().id,
            patient_id=current_user.id
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect('/profile')
