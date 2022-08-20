from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from user.database.models.BaseModel import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class CRUDBase:
    def get(
            self, 
            db: Session, 
            *, 
            skip: int = 0, 
            limit: int = 100,
            where_clause: Optional[] = None) -> List[ModelType]:
        query = db.query(self.model)
        if where_clause:
            query = db.query(self.model).filter(where_clause)
        return query.offset(skip).limit(limit).all()

    def update():
        pass