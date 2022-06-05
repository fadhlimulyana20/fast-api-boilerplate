from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import auth as authSchema, user as userSchema
from crud import user as userCrud
from api.deps import get_db, get_current_user
from utils.jwt import Jwt
from utils.password import PasswordUtils

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/login', response_model=authSchema.AuthResponse)
def login(auth: authSchema.AuthLogin = Depends(), db: Session = Depends(get_db)):
    user = userCrud.get_user_by_email(db, auth.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    password_match = PasswordUtils.compare(user.password, auth.password)
    if password_match:
        access_token = Jwt.create_token(data={"sub": user.email})
        data = authSchema.AuthResponse(access_token=access_token, token_type="bearer")
        return data

@router.get('/me', response_model=userSchema.User)
def read_current_user(user: userSchema.User = Depends(get_current_user)):
    return user
    