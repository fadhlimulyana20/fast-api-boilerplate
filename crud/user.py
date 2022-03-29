from sqlalchemy.orm import Session
from models import user
from schemas import user as userSchema


def get_user(db: Session, user_id: int):
    return db.query(user.User).filter(user.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user.User).filter(user.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user.User).offset(skip).limit(limit).all()


def create_user(db: Session, userInput: userSchema.UserCreate):
    fake_hashed_password = userInput.password + "notreallyhashed"
    db_user = user.User(email=userInput.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user