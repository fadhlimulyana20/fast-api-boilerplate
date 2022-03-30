from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.base import Base
from models.item import Items

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)
    name = Column(String(20))
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)

    items = relationship("Items", back_populates="owner")