import os
from typing import List
import alembic
from fastapi import Depends, FastAPI, HTTPException
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


@app.get('/')
async def root():
    return {"message": "Hello World!"}


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
