from datetime import date as Date
from typing import Optional

from pydantic import BaseModel


class CreateSchema(BaseModel):
    external_id: Optional[str] = None
    email: str
    first_name: str
    last_name: str
    phone_number: Optional[Date] = None
