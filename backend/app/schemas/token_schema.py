from pydantic import BaseModel
from typing import Optional


class BaseToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
