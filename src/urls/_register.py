from flask import render_template, redirect, Request, Response
from flask_login import current_user

from src.db import db
from src.models import User
from src.urls._base import BaseUrl

__all__ = ['RegisterUrl']


class RegisterUrl(BaseUrl):
    url = '/register'

    def get(self, request):
        if current_user.is_authenticated:
            return redirect('/')
        return render_template('register.html')

    def post(self, request):
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username):
            return 'Username already Present'

        user = User(username=username)  # FIXME: add __init__
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/auth')
