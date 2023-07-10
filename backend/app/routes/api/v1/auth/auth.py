from fastapi import Depends, APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.Config import configs
from app.oauth2 import create_access_token
from app.schemas.token_schema import BaseToken
from datetime import timedelta
from app.services import verify_hash
from app.db import get_admin_collection


router = APIRouter()

ADMIN_COL = get_admin_collection()


@router.post('/admin', response_model=BaseToken)
async def login_admin(admin_credentials: OAuth2PasswordRequestForm = Depends()):
    admin_exist = ADMIN_COL.find_one(
        {"email": admin_credentials.username})
    if admin_exist:
        if verify_hash(admin_credentials.password, admin_exist["password"]):
            expire_time = timedelta(minutes=int(
                configs.ACCESS_TOKEN_EXPIRE_MINUTES))
            token = create_access_token(
                data={"email": admin_exist["email"]}, expires_delta=expire_time)
            return {"access_token": token, "token_type": "Bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials.")
