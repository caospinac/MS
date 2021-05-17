import functools
import json

from redis import Redis

from lib.const import REDIS_HOST, REDIS_PASSWORD


client = Redis(host=REDIS_HOST, password=REDIS_PASSWORD)


def build_key(*sections):
    return '_'.join(filter(bool, sections))


def save(key: str, payload, **kwargs):
    client.set(key, json.dumps(payload), **kwargs)


def load(key: str):
    data = client.get(key)

    return data and json.loads(data)


def cached(wrapped):

    @functools.wraps(wrapped)
    def wrapper(*args, cache_key, **kwargs):
        result = client.get(cache_key)

        if not result:
            result = wrapped(*args, **kwargs)
            save(cache_key, result)

        return result

    return wrapper
