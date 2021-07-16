from flask import render_template
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from src.db import db
from src.models import User, Doctor, Specialty
from src.urls.base import BaseUrl


class RegisterDocUrl(BaseUrl):
    url = '/register_doc'

    def get(self, request):
        return render_template('register_doc.html')

    def post(self, request):
        form = dict(request.form)
        username = form['username']
        password = form.pop('password')

        if User.query.filter_by(username=username).first():
            return render_template('register_doc.html', error_username=True, **form)

        specialty = form.pop('specialty')
        if (specialty := Specialty.query.filter_by(title=specialty).first()) is None:
            specialty = Specialty(title=specialty)
            db.session.add(specialty)
            db.session.commit()
        doctor = Doctor(**(form | {'specialty_id': specialty.id}))  # FIXME: add __init__
        doctor.set_password(password)
        db.session.add(doctor)
        db.session.commit()
        return redirect('/doctors')
