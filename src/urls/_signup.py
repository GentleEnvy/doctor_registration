from datetime import date, timedelta

from flask import render_template, redirect

from src.models import Doctor, RecordTime
from src.urls.base import BaseUrl

__all__ = ['SignupUrl']


class SignupUrl(BaseUrl):
    url = '/signup'

    def get(self, request):
        if doctor_id := request.args.get('doctor'):
            return render_template(
                'signup.html',
                doctor=Doctor.query.filter_by(id=doctor_id).first(),
                today=date.today(), timedelta=timedelta,
                RecordTime=RecordTime
            )
        return redirect(self.url + f'?doctor={Doctor.query.first().id}')
