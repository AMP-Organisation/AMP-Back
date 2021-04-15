from ..crud.crud_base import CRUDBase
from ..database.models.active_ingredient_model import Active_Ingredient
from ..schemas.medicine_schema import CreatePrincipleActive, UpdatePrincipleActive


class CRUDMedicine(CRUDBase[Active_Ingredient, CreatePrincipleActive, UpdatePrincipleActive]):
    pass


medicine = CRUDMedicine(Active_Ingredient)
