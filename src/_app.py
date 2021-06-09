from typing import Final

from flask import Flask

__all__ = ['app']

app: Final[Flask] = Flask(__name__)
