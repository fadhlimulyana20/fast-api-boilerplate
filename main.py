from datetime import timedelta
import os
from typing import List
import alembic
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uvicorn

from models import base
from database.db import engine
from api.api import api_router
from config import settings

if settings.get_env().env == "development":
    print("Delevelopment mode")
    print("Running Migration")
    migration = os.system("alembic upgrade head")
    print(migration)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get('/')
async def root():
    return {"message": "Hello World!"}

@app.get('/test')
async def read_test(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/info")
async def info(settings: settings.Env = Depends(settings.get_env)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "db_name": settings.db_name
    }

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
