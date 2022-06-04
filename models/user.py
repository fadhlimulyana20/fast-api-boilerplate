from email.policy import default
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from models import Base
from models.item import Item
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base

# Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(150))
    password = Column(String(200))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    is_active = Column(Boolean, default=True)

    # items = relationship("Items", back_populates="owner")