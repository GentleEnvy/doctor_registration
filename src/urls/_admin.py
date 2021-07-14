from flask import render_template, redirect
from flask_login import current_user

from src.urls.base import BaseUrl

__all__ = ['AdminUrl']


class AdminUrl(BaseUrl):
    url = '/admin'

    def get(self, request):
        if hasattr(current_user, 'admin'):
            return render_template('adminp.html')
        return redirect('/')
