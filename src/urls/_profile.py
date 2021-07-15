from datetime import date, timedelta

from flask import render_template

from src.models import RecordTime
from src.urls.base import BaseUrl

__all__ = ['ProfileUrl']


class ProfileUrl(BaseUrl):
    url = '/profile'

    def get(self, request):
        return render_template(
            'profile.html',
            today=date.today(), timedelta=timedelta,
            RecordTime=RecordTime
        )
