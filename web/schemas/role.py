from pydantic import BaseModel


class CreateSchema(BaseModel):
    name: str
    code: str
    organization_id: str
