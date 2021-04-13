from typing import Optional

from sqlalchemy.orm import Session

from ..crud.crud_base import CRUDBase
from ..database.models.pillbox_model import Pillbox
from ..database.models.user_model import Users
from ..schemas.pillbox_schema import CreatePillbox, UpdatePillbox


class CRUDPillbox(CRUDBase[Pillbox, CreatePillbox, UpdatePillbox]):

    def getPillboxUser(self, db: Session, *, idUser: int) -> Optional[Pillbox]:
        find_relation = db.query(self.model).filter_by(user_id=idUser).all()
        return find_relation


pillbox = CRUDPillbox(Pillbox)
