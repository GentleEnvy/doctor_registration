from flask import render_template, Response

from src.urls._base_url import BaseUrl


class AuthUrl(BaseUrl):
    url = '/auth'

    def get(self, request):
        return Response(render_template('auth.html'))

    def post(self, request):
        pass
