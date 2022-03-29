from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import base
from database.db import engine
from api.api import api_router

base.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World!"}

app.include_router(api_router)