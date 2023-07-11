from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.token_schema import TokenData
from fastapi.exceptions import HTTPException
from app.Config import configs as settings
from app.db import get_admin_collection
from app.utils.serializer import serializeDict


ADMIN_COL = get_admin_collection()

oauth2_scheme_admin = OAuth2PasswordBearer(
    tokenUrl="/api/v1" + '/auth/admin', scheme_name="ADMIN LOGIN")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        email = payload.get("email")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        token_data = TokenData(
            **payload)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    return token_data


def get_current_admin(token: str = Depends(oauth2_scheme_admin)):
    token = verify_token(token)
    user = ADMIN_COL.find_one(
        {"email": token.email})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    return serializeDict(user)
