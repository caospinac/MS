import functools
import json
from typing import Any, Callable, TypeVar, cast

from redis import Redis

from lib.const import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


client = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def build_key(*sections: str) -> str:
    return '_'.join(filter(bool, sections))


def save(key: str, payload: Any, **kwargs: Any) -> None:
    client.set(key, json.dumps(payload), **kwargs)


def load(key: str) -> Any:
    data = client.get(key)

    return data and json.loads(data)


TFun = TypeVar('TFun', bound=Callable[..., Any])


def cached(wrapped: TFun) -> TFun:

    @functools.wraps(wrapped)
    def wrapper(cache_key: str, *args: Any, **kwargs: Any) -> Any:
        result = client.get(cache_key)

        if not result:
            result = wrapped(*args, **kwargs)
            save(cache_key, result)

        return result

    return cast(TFun, wrapper)
