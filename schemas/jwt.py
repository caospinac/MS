from typing import Optional

from pydantic import BaseModel


class TokenData(BaseModel):
    uid: str
    sid: str
    exp: Optional[str]
