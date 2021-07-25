import secrets
from typing import Dict

from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.auth import LoginSchema
from lib import Jwt, Redis
from models import Organization, User


def authenticate(db: Session, oid: str, payload: LoginSchema) -> Dict:
    org = Organization.get(db, oid)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    user = User.get_by_email(db, oid, payload.urs)
    err = True
    if user is None:
        User.dummy_password_check()
    elif user.check_password(payload.pwd):
        err = False

    if err:
        raise HTTPException(403, 'Incorrect credentials')

    assert user

    sid = secrets.token_hex(4)
    uid = str(user.id)
    token, expires_at = Jwt.generate_token(uid, sid)
    refresh_token = Jwt.generate_refresh_token(uid, sid)

    Redis.save(
        Redis.build_key('session', uid, sid),
        {
            # user info
            'id': uid,
        },
    )

    return {
        'token': token,
        'refresh_token': refresh_token,
        'expires_at': expires_at,
    }
