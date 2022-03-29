
from typing import List
from fastapi import APIRouter, Depends
from schemas import item as itemSchema
from crud import item as itemCrud
from api.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/items/", response_model=List[itemSchema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = itemCrud.get_items(db, skip=skip, limit=limit)
    return items
