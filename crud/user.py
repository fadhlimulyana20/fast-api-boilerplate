from sqlalchemy.orm import Session
from models import user
from schemas import user as userSchema
from utils import PasswordUtils


def get_user(db: Session, user_id: int):
    return db.query(user.User).filter(user.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> user.User | None:
    return db.query(user.User).filter(user.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.User).offset(skip).limit(limit).all()


def create_user(db: Session, userInput: userSchema.UserCreate):
    hashed_password = PasswordUtils.hash(userInput.password)
    db_user = user.User(email=userInput.email, name=userInput.name, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user