from typing import Optional, Any

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..crud.crud_base import CRUDBase
from ..database.models.pillbox_model import Pillbox
from sqlalchemy.orm.attributes import flag_modified
from ..schemas.pillbox_schema import CreatePillbox, UpdatePillbox


class CRUDPillbox(CRUDBase[Pillbox, CreatePillbox, UpdatePillbox]):

    def getPillboxUser(self, db: Session, *, idUser: int) -> Optional[Pillbox]:
        find_relation = db.query(self.model).filter_by(user_id=idUser).all()
        return find_relation

    @staticmethod
    def addTreatment(db: Session, updated_pillbox: Any, ori_pillbox: Any):
        if updated_pillbox.list_treatment not in ori_pillbox.list_treatment:
            ori_pillbox.list_treatment.append(updated_pillbox.list_treatment)
            flag_modified(ori_pillbox, 'list_treatment')
            db.commit()
            db.refresh(ori_pillbox)
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ce traitement fait déjà parti de ce pillulier",
            )
        return ori_pillbox

    def verifyPillbox(self, db: Session, pillbox_in: CreatePillbox):
        pillbox_found = db.query(self.model).filter_by(user_id=pillbox_in.user_id).all()
        result = False
        for pillbox in pillbox_found:
            if pillbox.name is pillbox_in.name:
                result = True
        return result
pillbox = CRUDPillbox(Pillbox)
