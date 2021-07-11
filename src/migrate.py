from typing import Final

from flask_migrate import Migrate

from src.app import app
from src.db import db

__all__ = ['migrate']

migrate: Final[Migrate] = Migrate(app, db, render_as_batch=True)
