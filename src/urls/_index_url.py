from flask import render_template, Response

from src.urls._base_url import BaseUrl

__all__ = ['IndexUrl']


class IndexUrl(BaseUrl):
    url = '/'

    def get(self, request):
        return Response(render_template('index.html'))
