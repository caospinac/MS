from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.user import CreateSchema, UpdateSchema, UpdatePasswordSchema

from models import Organization, User
from db import use_db


@use_db
def get_list(oid: str, db: Session = None):
    org = Organization.get(db, oid)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    return org.users


def get(db: Session, ident: str):
    user = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    return user


@use_db
def create(oid: str, payload: CreateSchema, db: Session = None):
    org: Organization = Organization.get(db, oid)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    user = User.get_by_email(db, oid, payload.email)
    if user is not None:
        raise HTTPException(400, 'Email already exists')

    if payload.external_id:
        user = User.get_by_external_id(db, oid, payload.external_id)
        if user is not None:
            raise HTTPException(400, 'The given ID already exists')

    user = User(
        organization=org,
        role=payload.role,
        external_id=payload.external_id,
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name,
        phone_number=payload.phone_number,
    )

    user.save(db)

    return user


@use_db
def update(ident: str, payload: UpdateSchema, db: Session = None):
    user: User = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    oid = user.organization_id
    if payload.external_id:
        user = User.get_by_external_id(db, oid, payload.external_id)
        if user is not None and user.id != ident:
            raise HTTPException(400, 'The given ID already exists')

    for key in payload.__fields_set__:
        setattr(user, key, getattr(payload, key))

    user.update(db)

    return user


@use_db
def delete(ident: str, db: Session = None):
    user: User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    user.delete(db)


@use_db
def restore(ident: str, db: Session = None):
    user = User.get(db, ident)
    if user is not None:
        raise HTTPException(400, 'Nothing to restore')

    user = User.restore(db, ident)
    if user is None:
        raise HTTPException(400, 'The user cannot be found in the database')

    return user


@use_db
def update_password(ident: str, payload: UpdatePasswordSchema,
                    db: Session = None):
    user = User.get(db, ident)
    if user is None:
        raise HTTPException(404, 'User not found')

    if user.status != User.STATUS_ACTIVE:
        raise HTTPException(400, 'User is not active')

    if not user.check_password(payload.old_password):
        raise HTTPException(403, 'Invalid password')

    user.set_password(payload.new_password)
    user.save(db)
