from datetime import date as Date
from typing import Optional

from pydantic import BaseModel


class CreateSchema(BaseModel):
    external_id: Optional[str] = None
    email: str
    password: str
    first_name: str
    last_name: str
    birthdate: Optional[Date] = None
    phone_number: Optional[Date] = None
    gender: Optional[Date] = None
    avatar: Optional[Date] = None
    role_id: str
