import os

from flask import Flask

__all__ = ['app']

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or '__secret__'
app.debug = bool(int(os.environ.get('DEBUG') or 0))
