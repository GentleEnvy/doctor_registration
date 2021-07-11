from flask import render_template, Response
from flask_login import login_required

from src.urls._base import BaseUrl

__all__ = ['IndexUrl']


class IndexUrl(BaseUrl):
    url = '/'

    def get(self, request):
        return Response(render_template('index.html'))

    def get_view(self):
        return login_required(super().get_view())
