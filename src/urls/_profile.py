from flask import render_template

from src.urls.base import BaseUrl

__all__ = ['ProfileUrl']


class ProfileUrl(BaseUrl):
    url = '/profile'

    def get(self, request):
        return render_template('profile.html')
