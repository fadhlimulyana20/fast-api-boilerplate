from sqlalchemy.orm import Session

from models import item
from schemas import item as itemSchema


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(item.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: itemSchema.ItemCreate, user_id: int):
    db_item = item.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item