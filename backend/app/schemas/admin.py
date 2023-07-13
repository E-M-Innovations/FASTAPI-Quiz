from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from app.models.admin import BaseAdmin


class AdminCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    model_config = ConfigDict(
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {
                "name": "string",
                "email": "string@example.com",
                "password": "string",
                "created_at": "datetime",
            }
        },
    )


class AdminOut(BaseAdmin):
    id: str = Field(alias="_id")
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "_id": "string",
                "email": "string@example.com",
                "name": "string",
                "created_at": "datetime",
            }
        },
    )
