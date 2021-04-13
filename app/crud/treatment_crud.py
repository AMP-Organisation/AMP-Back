from typing import List

from sqlalchemy.orm import Session

from ..crud.crud_base import CRUDBase
from ..database.models.treatment_model import Treatment
from ..schemas.treatment_schema import CreateTreatment, UpdateTreatment


class CRUDTreatment(CRUDBase[Treatment, CreateTreatment, UpdateTreatment]):

    def related_treatment(self, db: Session, all_treatment=List[int]) -> List[Treatment]:
        all_treatment = [db.query(self.model).get(current_id) for current_id in all_treatment]
        return all_treatment
    pass


treatment = CRUDTreatment(Treatment)
