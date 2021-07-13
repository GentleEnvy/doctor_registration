from src.db import db

__all__ = ['Specialty']


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
