from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from app.models.admin import Admin


class AdminCreate(BaseModel):
    email: EmailStr
    name: str

    model_config = ConfigDict(
        str_strip_whitespace=True, json_schema_extra={
            "example": {
                "email": "nk@example.com",
                "name": "Neeraj Kumar",
                "created_at": "2023-07-09T18:13:50.833+00:00"
            }
        })


class AdminOut(Admin):
    id: str = Field(alias="_id")
    model_config = ConfigDict(from_attributes=True, populate_by_name=True, json_schema_extra={
        "example": {
            "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
            "email": "nk@example.com",
            "name": "Neeraj Kumar",
            "created_at": "2023-07-09T18:13:50.833+00:00"
        }
    })
