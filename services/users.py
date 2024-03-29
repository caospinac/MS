from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from schemas.user import CreateSchema, UpdateSchema, UpdatePasswordSchema
from models import Organization, User


def get_list(db: Session, oid: str) -> List[User]:
    org = Organization.get(db, oid)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    return org.users


def get(db: Session, ident: str) -> User:
    user = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    return user


def create(db: Session, oid: str, payload: CreateSchema) -> User:
    org = Organization.get(db, oid)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    user = User.get_by_email(db, oid, payload.email)
    if user is not None:
        raise HTTPException(400, 'Email already exists')

    if payload.external_id:
        user = User.get_by_external_id(db, oid, payload.external_id)
        if user is not None:
            raise HTTPException(400, 'The given ID already exists')

    user = User(organization=org)

    for key in payload.__fields_set__:
        setattr(user, key, getattr(payload, key))

    user.save(db)

    return user


def update(db: Session, ident: str, payload: UpdateSchema) -> User:
    user = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    oid = user.organization_id
    if payload.external_id:
        temp_user = User.get_by_external_id(db, oid, payload.external_id)
        if temp_user is not None and temp_user.id != ident:
            raise HTTPException(400, 'The given ID already exists')

    for key in payload.__fields_set__:
        setattr(user, key, getattr(payload, key))

    user.update(db)

    return user


def delete(db: Session, ident: str) -> None:
    user = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    user.delete(db)


def restore(db: Session, ident: str) -> User:
    user = User.get(db, ident)
    if user is not None:
        raise HTTPException(400, 'Nothing to restore')

    user = User.restore(db, ident)
    if user is None:
        raise HTTPException(400, 'The user cannot be found in the database')

    return user


def update_password(
    db: Session, ident: str, payload: UpdatePasswordSchema,
) -> None:
    user = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    if user.status != User.STATUS_ACTIVE:
        raise HTTPException(400, 'User is not active')

    if not user.check_password(payload.old_password):
        raise HTTPException(403, 'Invalid password')

    user.set_password(payload.new_password)
    user.save(db)
