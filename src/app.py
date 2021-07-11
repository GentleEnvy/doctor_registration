import os
from typing import Final

from flask import Flask

__all__ = ['app']

app: Final[Flask] = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
