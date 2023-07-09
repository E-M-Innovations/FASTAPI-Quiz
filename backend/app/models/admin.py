from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class Admin(BaseModel):
    email: EmailStr
    name: str
    created_at: datetime

    model_config = ConfigDict(
        str_strip_whitespace=True, json_schema_extra={
            "example": {
                "email": "nk@example.com",
                "name": "Neeraj Kumar",
                "created_at": "2023-07-09T18:13:50.833+00:00"
            }
        })
