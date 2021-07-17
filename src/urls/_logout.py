from flask import redirect
from flask_login import logout_user

from src.urls.base import BaseUrl

__all__ = ['LogoutUrl']


class LogoutUrl(BaseUrl):
    url = '/logout'

    def get(self, request):
        logout_user()
        return redirect('http://www2.cs.vsu.ru/~komarov_s_o/cgi-bin/mydb/mydb.cgi')
