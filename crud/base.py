from ctypes import Union
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar
from models import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]) -> None:
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
    
    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Select data by id.

        **Parameters**
        * `db` : SQLAlchemy session
        * `id` : Primary Key
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_many(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Select many datas.

        **Parameters**
        * `db` : SQLAlchemy session
        * `skip` : skip
        * `limit` : limit
        """
        return db.query(self.model).offset(skip).limit(limit).all()
    
    def create(self, db: Session, data: CreateSchemaType) -> ModelType:
        """
        Select many datas.

        **Parameters**
        * `db` : SQLAlchemy session
        * `data` : Pydantic object
        """
        data_json = jsonable_encoder(data)
        db_obj = self.model(**data_json)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, id: Any, data_in: UpdateSchemaType) -> ModelType:
        data = db.query(self.model).filter(self.model.id == id).first()
        # data = jsonable_encoder(data)
        print(data)
        if not isinstance(data_in, dict):
            data_in = jsonable_encoder(data_in)

        for field in data_in:
            setattr(data, field, data_in[field])
        
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    
    def remove(self, db: Session, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
