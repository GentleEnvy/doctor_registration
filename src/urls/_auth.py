from flask import render_template, redirect
from flask_login import current_user, login_user

from src.models import User
from src.urls.base import BaseUrl

__all__ = ['AuthUrl']


class AuthUrl(BaseUrl):
    url = '/auth'

    def get(self, request):
        if current_user.is_authenticated:
            return redirect('/')
        return render_template('auth.html')

    def post(self, request):
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/')
        return render_template('auth.html', error_username_or_password=True)
