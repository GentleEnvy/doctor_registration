from flask import render_template, Response
from flask_login.mixins import AnonymousUserMixin
from src.urls._base import BaseUrl

__all__ = ['IndexUrl']


class IndexUrl(BaseUrl):
    url = '/'

    def get(self, request):
        return Response(render_template('index.html'))
