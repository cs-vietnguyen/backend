from typing import Any, Dict

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


class Manager:
    def __init__(self, model) -> None:
        self.model = model

    def create(self, obj, db: Session):
        obj_model = self.model(**obj.__dict__)
        db.add(obj_model)
        db.commit()
        db.refresh(obj_model)
        return obj_model

    def update(self, obj, db: Session, *args, **kwargs):
        json_obj: Dict[str, Any] = jsonable_encoder(obj)
        for field, value in kwargs.items():
            if field in json_obj:
                setattr(obj, field, value)

        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
