from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base

from utils.string import StringUtils

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return f"{StringUtils.snake_case(cls.__name__)}s"

# Base = declarative_base()