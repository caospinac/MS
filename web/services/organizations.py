from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Organization, Role, User
from schemas.organization import CreateSchema
from db import use_db


@use_db
def create(payload: CreateSchema, db: Session=None):

    existing_org = Organization.get_by_prefix(db, payload.prefix)
    if existing_org:
        raise HTTPException(400, 'Prefix not available')

    organization = Organization(name=payload.name, prefix=payload.prefix)
    role = Role(code='owner')
    user = User(**payload.owner.__dict__)

    role.users.append(user)
    organization.roles.append(role)

    organization.save(db)

    return organization


@use_db
def get_list(db: Session=None):

    return Organization.get_list(db)
