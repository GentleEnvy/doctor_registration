from flask import render_template

from src.models import Doctor
from src.urls.base import BaseUrl

__all__ = ['DoctorsUrl']


class DoctorsUrl(BaseUrl):
    url = '/doctors'

    def get(self, request):
        return render_template('specialists.html', doctors=Doctor.query.all())
