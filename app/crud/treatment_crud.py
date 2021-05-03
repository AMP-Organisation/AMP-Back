from typing import List

from sqlalchemy.orm import Session

from ..crud.crud_base import CRUDBase
from ..database.models.treatment_model import Treatment
from ..database.models.pillbox_model import Pillbox
from ..database.models.medicine_model import medicine
from ..schemas.treatment_schema import CreateTreatment, UpdateTreatment


class CRUDTreatment(CRUDBase[Treatment, CreateTreatment, UpdateTreatment]):

    def related_treatment(self, db: Session, all_treatment=List[int]) -> List[Treatment]:
        all_treatment = [db.query(self.model).get(current_id) for current_id in all_treatment]
        return all_treatment

    def user_treatment(self, db: Session, user_id=int) -> List[Treatment]:
        all_treatment_user = db.query(self.model).filter_by(user_id=user_id).all()
        return all_treatment_user

    def related_medicine(self, db: Session, current_treatment=int) -> List[medicine]:
        treatment = db.query(self.model).get(current_treatment)
        all_medicine = [db.query(medicine).get(medicine_id) for medicine_id in treatment.medicine_id]
        return all_medicine
    pass


treatment = CRUDTreatment(Treatment)
