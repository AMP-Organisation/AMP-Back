from ..crud.crud_base import CRUDBase
from ..database.models.treatment_model import Treatment
from ..schemas.treatment_schema import CreateTreatment, UpdateTreatment


class CRUDTreatment(CRUDBase[Treatment, CreateTreatment, UpdateTreatment]):
    pass


treatment = CRUDTreatment(Treatment)
