from datetime import time

from flask import render_template
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from src.db import db
from src.models import User, Doctor, Specialty, RecordTime
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

        form_specialty = form.pop('specialty')
        specialty = Specialty.query.filter_by(title=form_specialty).first()
        if specialty is None:
            specialty = Specialty(title=form_specialty)
            db.session.add(specialty)
            db.session.commit()
        form['specialty_id'] = specialty.id
        doctor = Doctor(**form)
        doctor.set_password(password)
        db.session.add(doctor)
        db.session.commit()
        for i in range(7):
            for h in range(8, 16):
                rt = RecordTime(doctor=doctor, weekday=i, start=time(h), end=time(h + 1))
                db.session.add(rt)
                db.session.commit()
        return redirect(
            'http://www2.cs.vsu.ru/~komarov_s_o/cgi-bin/mydb/mydb.cgi/doctors'
        )
