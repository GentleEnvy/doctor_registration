from typing import Final

from flask_sqlalchemy import SQLAlchemy

from src.app import app

__all__ = ['db']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
db: Final[SQLAlchemy] = SQLAlchemy(app)
