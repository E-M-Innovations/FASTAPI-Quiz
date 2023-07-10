from pydantic import BaseModel, EmailStr
from datetime import datetime


class BaseAdmin(BaseModel):
    email: EmailStr
    name: str
    created_at: datetime


class Admin(BaseAdmin):
    password: str
