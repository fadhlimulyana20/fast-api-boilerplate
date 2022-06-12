from fastapi import APIRouter
from api.endpoints import user, item, auth


api_router = APIRouter()
v1_api_router = APIRouter(prefix='/v1')

# V1 Router
v1_api_router.include_router(user.router)
v1_api_router.include_router(auth.router)

# Main Router 
api_router.include_router(v1_api_router)


# api_router.include_router(item.router)
