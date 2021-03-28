from fastapi import HTTPException
from sqlalchemy.orm import Session
from schemas.user import CreateSchema

from models import Organization, Role, User
from db import use_db


@use_db
def get_list(oid: str, db: Session = None):
    org = Organization.get(db, oid)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    return org.users


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

    role_code = payload.role_code or Role.C_DEFAULT
    role = Role.get_by_code(db, oid, role_code)
    if role is None:
        raise HTTPException(404, f'The role code {role_code} does not exists')

    user = User(
        organization=org,
        role=role,
        external_id=payload.external_id,
        email=payload.email,
        first_name=payload.first_name,
        last_name=payload.last_name,
        phone_number=payload.phone_number,
    )

    user.save(db)

    return user
