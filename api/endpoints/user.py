from http.client import HTTPException
from typing import List
from fastapi import APIRouter, Depends
from schemas import user as userSchema, item as itemSchema
from crud import user as userCrud, item as itemCrud
from api.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/users/", response_model=userSchema.User)
def create_user(user: userSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = userCrud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userCrud.create_user(db=db, userInput=user)


@router.get("/users/", response_model=List[userSchema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCrud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=userSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# @router.post("/users/{user_id}/items/", response_model=userSchema.Item)
# def create_item_for_user(
#     user_id: int, item: itemSchema.ItemCreate, db: Session = Depends(get_db)
# ):
#     return itemCrud.create_user_item(db=db, item=item, user_id=user_id)