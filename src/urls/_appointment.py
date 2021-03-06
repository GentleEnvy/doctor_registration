from datetime import date as python_date
from datetime import time as python_time

from werkzeug.utils import redirect
from flask_login import current_user

from src.db import db
from src.models import Appointment, Doctor, RecordTime
from src.urls.base import BaseUrl

__all__ = ['AppointmentUrl']


class AppointmentUrl(BaseUrl):
    url = '/signup/appointment'

    def get(self, request):
        start = python_time.fromisoformat(request.args['start'])
        date = python_date.fromisoformat(request.args['date'])
        doctor_id = request.args['doctor']
        appointment = Appointment(
            record_time_id=RecordTime.query.filter_by(
                start=start,
                doctor_id=Doctor.query.filter_by(id=doctor_id).first().id,
                weekday=date.weekday()
            ).first().id,
            date=date,
            patient_id=current_user.id
        )
        db.session.add(appointment)
        db.session.commit()
        return redirect('http://www2.cs.vsu.ru/~komarov_s_o/cgi-bin/mydb/mydb.cgi'
                        '/profile')
