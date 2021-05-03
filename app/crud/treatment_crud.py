from typing import List

from sqlalchemy.orm import Session

from ..crud.crud_base import CRUDBase
from ..database.models.treatment_model import Treatment
<<<<<<< HEAD
from ..database.models.pillbox_model import Pillbox
=======
>>>>>>> :construction: added routes to get related medicine for a treatment + database modifications
from ..database.models.medicine_model import medicine
from ..schemas.treatment_schema import CreateTreatment, UpdateTreatment


class CRUDTreatment(CRUDBase[Treatment, CreateTreatment, UpdateTreatment]):

    def related_treatment(self, db: Session, all_treatment=List[int]) -> List[Treatment]:
        all_treatment = [db.query(self.model).get(current_id) for current_id in all_treatment]
        return all_treatment

<<<<<<< HEAD
    def user_treatment(self, db: Session, user_id=int) -> List[Treatment]:
        all_treatment_user = db.query(self.model).filter_by(user_id=user_id).all()
        return all_treatment_user

=======
>>>>>>> :construction: added routes to get related medicine for a treatment + database modifications
    def related_medicine(self, db: Session, current_treatment=int) -> List[medicine]:
        treatment = db.query(self.model).get(current_treatment)
        all_medicine = [db.query(medicine).get(medicine_id) for medicine_id in treatment.medicine_id]
        return all_medicine

    def verify_name(self, db:Session, user_id: int, name: str) -> bool:
        check_treatement = db.query(self.model).filter_by(user_id=user_id).all()
        result = False
        for user_treatment in check_treatement:
            if user_treatment.name is name:
                result = True
        return result


treatment = CRUDTreatment(Treatment)
