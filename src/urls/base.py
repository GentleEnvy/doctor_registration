from abc import ABC, abstractmethod
from http import HTTPStatus

from flask import Request, request as flask_request

from src.app import app

__all__ = ['BaseUrl']


class BaseUrl(ABC):
    def __init__(self):
        app.add_url_rule(
            rule=self.url,
            endpoint=self.__class__.__name__,
            view_func=self.get_view(),
            methods=['GET', 'POST']
        )

    def get_view(self):
        def view():
            request: Request = flask_request
            # noinspection PyBroadException
            try:
                method = request.method.upper()
                if method == 'GET':
                    response = self.get(request)
                else:  # POST
                    response = self.post(request)
            except Exception:
                if app.debug:
                    raise
                response = app.make_response('Error')
                response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
            return response

        return view

    @property
    @abstractmethod
    def url(self) -> str:
        raise NotImplementedError

    def get(self, request: Request):
        return app.make_response('Not supported')

    def post(self, request: Request):
        return app.make_response('Not supported')
