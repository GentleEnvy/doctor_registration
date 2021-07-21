from flask import redirect

from src.db import db
from src.models import Appointment
from src.urls.base import BaseUrl

__all__ = ['DeleteAppointmentUrl']


class DeleteAppointmentUrl(BaseUrl):
    url = '/delete_appointment'
    
    def get(self, request):
        appointment_id = request.args.get('id')
        if appointment_id is not None:
            try:
                appointment = Appointment.query.filter_by(id=appointment_id).first()
                db.session.delete(appointment)
                db.session.commit()
            except Exception:
                pass
        return redirect(
            'http://www2.cs.vsu.ru/~komarov_s_o/cgi-bin/mydb/mydb.cgi/profile'
        )
