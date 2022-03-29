from fastapi import APIRouter
from api.endpoints import user, item


api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(item.router)
