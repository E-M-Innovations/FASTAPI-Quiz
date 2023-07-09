from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from app.models.admin import Admin
from app.db import get_admin_collection
from app.schemas.admin import AdminCreate, AdminOut
from app.utils.serializer import serializeDict
from datetime import datetime

router = APIRouter()
ADMIN_COL = get_admin_collection()


@router.post("/", response_description="Create new admin",
             status_code=status.HTTP_201_CREATED, response_model=AdminOut)
async def create_admin(req: Request, admin: AdminCreate):
    admin_exist = ADMIN_COL.find_one(
        {"email": admin.email})
    if admin_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=f"User with email {admin.email} already exist.")
    admin = Admin(
        created_at=datetime.now(), **admin.model_dump())
    _id = ADMIN_COL.insert_one(
        admin.model_dump())

    return_admin = ADMIN_COL.find_one(
        _id.inserted_id)

    return serializeDict(return_admin)


# @router.get("/me", response_description="Get me details",
#             status_code=status.HTTP_200_OK, response_model=AdminOut)
# async def get_current_admin(req: Request):
#     return {}
