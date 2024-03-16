from typing import Any, Dict, Optional, Union

from sqlalchemy import text
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.user import Users
from schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    # def get(self, db: Session, id: Any) -> Optional[ModelType]:
    #     return db.query(Users).filter(Users.id == id).first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[Users]:
        return db.query(Users).filter(Users.username == username).first()

    # def create(self, db: Session, *, obj_in: UserCreate) -> User:
    #     db_obj = User(
    #         username=obj_in.username,
    #     )
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    # def update(
    #     self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    # ) -> User:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.model_dump(exclude_unset=True)
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)


user = CRUDUser(Users)
