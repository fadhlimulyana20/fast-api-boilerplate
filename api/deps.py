# Dependency
from fastapi import Depends, HTTPException, status
from database.db import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from crud import user as userCrud

from utils.jwt import Jwt

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = Jwt.decode_token(token)
    if not payload:
        raise credentials_exception
    email: str = payload.get('sub')
    user = userCrud.get_user_by_email(email=email)
    if not user:
        raise credentials_exception
    return user