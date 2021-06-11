from datetime import datetime

from ..crud.crud_base import CRUDBase
from ..database.models.user_model import Users
from ..schemas.auth_schema import LoginBase, RegisterBase
from sqlalchemy.orm import Session
from ..auth import security
from typing import Optional


class CRUDAuth(CRUDBase[Users, RegisterBase, LoginBase]):

    def login(self, db: Session, email: str, password: str) -> Optional[Users]:
        current_user = db.query(self.model).filter_by(email=email).first()
        password_check = security.encryption.check_encrypted_password(password, current_user.password)
        if password_check:
            return current_user

        return password_check

    def register(self, db: Session, user: RegisterBase) -> Optional[Users]:
        user.password = security.encryption.encrypt_password(user.password)
        user.dt_inscription = datetime.now()
        return self.create(db=db, obj_in=user)


auth = CRUDAuth(Users)
