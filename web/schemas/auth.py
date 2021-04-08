from pydantic import BaseModel


class LoginSchema(BaseModel):
    urs: str
    pwd: str
