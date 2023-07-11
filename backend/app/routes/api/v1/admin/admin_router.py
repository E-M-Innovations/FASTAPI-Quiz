from fastapi import APIRouter, status, Depends
from fastapi.requests import Request
from app.schemas.admin import AdminCreate, AdminOut
from app.utils.serializer import serializeDict
from app.oauth2 import get_current_admin
from app.services import service_admin_create_account

router = APIRouter()


@router.post("/", response_description="Create new admin",
             status_code=status.HTTP_201_CREATED, response_model=AdminOut)
async def create_admin(req: Request, admin: AdminCreate):
    return service_admin_create_account(admin)


@router.get("/me", response_description="Get me details",
            status_code=status.HTTP_200_OK, response_model=AdminOut)
async def whoami(req: Request, current_admin=Depends(get_current_admin)):
    return serializeDict(current_admin)
