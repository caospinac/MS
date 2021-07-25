from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Organization, User
from schemas.organization import CreateSchema, CompleteCreationSchema


def create(db: Session, payload: CreateSchema) -> Organization:
    existing_org = Organization.get_by_prefix(db, payload.prefix)
    if existing_org:
        raise HTTPException(400, 'Prefix not available')

    organization = Organization(name=payload.name, prefix=payload.prefix)
    user = User(**payload.owner.__dict__, role=User.ROLE_BASIC)

    organization.users.append(user)

    organization.save(db)

    return organization


def get_list(db: Session) -> List[Organization]:
    return Organization.get_list(db)


def get(db: Session, ident: str) -> Organization:
    org = Organization.get(db, ident)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    return org


def complete_creation(
    db: Session, ident: str, payload: CompleteCreationSchema,
) -> Organization:
    org = Organization.get(db, ident)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    owner: User = org.users[0]

    org.status = Organization.STATUS_ACTIVE
    owner.status = User.STATUS_ACTIVE
    owner.set_password(payload.password)

    org.update(db)

    return org
