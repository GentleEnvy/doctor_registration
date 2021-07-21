from flask import redirect

from flask import redirect

from src.db import db
from src.models import Patient
from src.urls.base import BaseUrl

__all__ = ['DeletePatientUrl']


class DeletePatientUrl(BaseUrl):
    url = '/delete_patient'
    
    def get(self, request):
        patient_id = request.args.get('id')
        if patient_id:
            try:
                patient = Patient.query.filter_by(id=patient_id).first()
                for appointment in patient.appointment_set:
                    db.session.delete(appointment)
                    db.session.commit()
                db.session.delete(patient)
                db.session.commit()
            except Exception:
                pass
        return redirect(
            'http://www2.cs.vsu.ru/~komarov_s_o/cgi-bin/mydb/mydb.cgi/profile'
        )
