from typing import Optional

from pydantic import BaseModel


class CreateSchema(BaseModel):
    external_id: Optional[str]
    email: str
    first_name: str
    last_name: str
    phone_number: Optional[str]
    role: Optional[str]


class UpdateSchema(BaseModel):
    external_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    role: Optional[str]


class UpdatePasswordSchema(BaseModel):
    old_password: str
    new_password: str
