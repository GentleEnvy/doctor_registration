from datetime import date, timedelta

from flask import render_template, redirect

from src.db import db
from src.models import Doctor, RecordTime, Patient
from src.urls.base import BaseUrl

__all__ = ['DeletePatientUrl']


class DeletePatientUrl(BaseUrl):
    url = '/delete_patient'
    
    def get(self, request):
        patient_id = request.args.get('id')
        if patient_id:
            try:
                patient = Patient.query.filter_by(id=patient_id).first()
                db.session.delete(patient)
                db.session.commit()
            except Exception:
                pass
        return redirect(
            'http://www2.cs.vsu.ru/~komarov_s_o/cgi-bin/mydb/mydb.cgi/profile'
        )
