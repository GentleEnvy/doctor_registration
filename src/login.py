from typing import Final

from flask_login import LoginManager

from src.app import app
from src.models import User

__all__ = ['login']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login: Final[LoginManager] = LoginManager(app)
login.login_view = 'AuthUrl'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
