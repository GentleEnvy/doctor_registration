from flask import render_template, Response

from src.urls._base import BaseUrl

__all__ = ['AuthUrl']


class AuthUrl(BaseUrl):
    url = '/auth'

    def get(self, request):
        return Response(render_template('auth.html'))

    def post(self, request):
        pass
