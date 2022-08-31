from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from uuid import UUID
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from user.database.models.BaseModel import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, connection: Session, model: Type[ModelType]):
        self._connection: Session = connection
        self.model: Type[ModelType] = model

    def create(self, *, obj_in: ModelType) -> ModelType:
        self._connection.add(obj_in)
        self._connection.commit()
        self._connection.refresh(obj_in)
        return obj_in

    def delete(self, *, id_: UUID) -> None:
        self._connection.query(self.model).filter(self.model.id == id_).delete()
        self._connection.commit()

    def get(self, *, skip: int = 0, limit: int = 100, where_clause: Any = None) -> List[ModelType]:
        query = self._connection.query(self.model)

        if where_clause is not None:
            query = query.filter(where_clause)

        return query.offset(skip).limit(limit).all()

    def update():
        pass
