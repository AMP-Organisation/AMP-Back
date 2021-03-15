from ..crud.crud_base import CRUDBase
from ..database.models.user_model import Users, Group
from ..schemas.user_schema import CreateUser, UpdateUser
from sqlalchemy.orm import Session
from typing import Optional


class CRUDUser(CRUDBase[Users, CreateUser, UpdateUser]):

    def get_by_username(self, db: Session, username: str) -> Optional[Users]:
        search_user = db.query(self.model).filter_by(username=username).first()
        return search_user

    @staticmethod
    def relation(db: Session, *, value: any) -> Optional[Users]:
        find_relation = db.query(Users).join(Group).filter(Group.Type == value).first()
        return find_relation


user = CRUDUser(Users)
