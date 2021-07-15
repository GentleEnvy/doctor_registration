from flask import render_template, redirect
from flask_login import current_user, login_user

from src.db import db
from src.models import User, Patient
from src.urls.base import BaseUrl

__all__ = ['RegisterUrl']


class RegisterUrl(BaseUrl):
    url = '/register'

    def get(self, request):
        if current_user.is_authenticated:
            return redirect('/')
        return render_template('register.html')

    def post(self, request):
        form = dict(request.form)
        username = form['username']
        password = form.pop('password')

        if User.query.filter_by(username=username).first():
            return render_template('register.html', error_username=True, **form)

        patient = Patient(**form)  # FIXME: add __init__
        patient.set_password(password)
        db.session.add(patient)
        db.session.commit()
        login_user(patient)
        return redirect('/')
