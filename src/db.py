from typing import Final

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, event

from src.app import app

__all__ = ['db']

_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

_metadata = MetaData(naming_convention=_convention)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: Final[SQLAlchemy] = SQLAlchemy(app, metadata=_metadata)
event.listen(db.engine, 'connect', lambda c, _: c.execute('pragma foreign_keys=on'))
