from flask import render_template

from src.urls._base_url import BaseUrl


class IndexUrl(BaseUrl):
    url = '/'

    def get(self, request):
        return render_template('index.html')
