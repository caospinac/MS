from inspect import iscoroutinefunction
import traceback

from typing import Any, Callable, Dict
import functools

from fastapi import APIRouter, HTTPException


class Router(APIRouter):

    def add_api_route(
        self, path: str, endpoint: Callable[..., Any], *argv: Any, **kw: Any,
    ) -> None:
        return super().add_api_route(path,
                                     self.handle_endpoint(endpoint),
                                     *argv, **kw)

    def handle_endpoint(self, func: Callable[..., Any]) -> Callable[..., Any]:

        @functools.wraps(func)
        async def wrapper(*argv: Any, **kw: Any) -> Dict:
            try:
                if iscoroutinefunction(func):
                    r = await func(*argv, **kw)
                else:
                    r = func(*argv, **kw)

            except Exception as e:
                print(traceback.format_exc())
                if isinstance(e, HTTPException):
                    raise e

                raise HTTPException(500) from e

            return {
                'data': r,
            }

        return wrapper
