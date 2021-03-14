from pydantic import BaseModel


class CreateSchema(BaseModel):
    prefix: str
    name: str
