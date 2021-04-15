from typing import List

from sqlalchemy.orm import Session

from ..crud.crud_base import CRUDBase
from ..database.models.active_ingredient_model import Active_Ingredient
from ..schemas.medicine_schema import CreatePrincipleActive, UpdatePrincipleActive


class CRUDMedicine(CRUDBase[Active_Ingredient, CreatePrincipleActive, UpdatePrincipleActive]):

    def get_all_principle_active(self, db: Session, all_id: List[int]) -> List[Active_Ingredient]:
        all_active_ingredient = [db.query(self.model).get(current_id) for current_id in all_id]
        return all_active_ingredient
    pass


medicine = CRUDMedicine(Active_Ingredient)
