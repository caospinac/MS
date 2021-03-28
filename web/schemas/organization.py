from pydantic import BaseModel


class OwnerUser(BaseModel):
    email: str
    first_name: str
    last_name: str


class CreateSchema(BaseModel):
    prefix: str
    name: str
    owner: OwnerUser
