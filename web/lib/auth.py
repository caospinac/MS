import uuid
from datetime import datetime, timedelta

import jwt

from lib.const import (
    ACCESS_TOKEN_KEY, REFRESH_ACCESS_TOKEN_KEY, TOKEN_EXPIRATION_SEC
)


def generate_token(user_id: str):
    exp = datetime.utcnow() + timedelta(seconds=TOKEN_EXPIRATION_SEC)
    token = jwt.encode(
        {
            'sid': uuid.uuid4().hex,
            'uid': user_id,
            'exp': exp,
        },
        ACCESS_TOKEN_KEY,
        algorithm='HS256',
    )

    return token, exp


def verify_token(encoded_data: str) -> dict:
    return jwt.decode(encoded_data, ACCESS_TOKEN_KEY, algorithm='HS256')


def generate_refresh_token(user_id: str):
    return jwt.encode(
        {'uid': user_id},
        REFRESH_ACCESS_TOKEN_KEY,
        algorithm='HS256'
    )


def verify_refresh_token(encoded_data: str) -> dict:
    return jwt.decode(encoded_data, REFRESH_ACCESS_TOKEN_KEY, algorithm='HS256')
