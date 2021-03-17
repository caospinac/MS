from typing import Any, Callable
import functools

from fastapi import APIRouter


class Router(APIRouter):

    def add_api_route(self, path, endpoint, *argv, **kw):
        return super().add_api_route(path,
                                     self.handle_endpoint(endpoint),
                                     *argv, **kw)

    def handle_endpoint(self, func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        def wrapper(*argv, **kw):
            r = func(*argv, **kw)
            return {
                'data': r
            }

        return wrapper
