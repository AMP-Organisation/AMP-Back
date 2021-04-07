from ..crud.crud_base import CRUDBase
from ..database.models.symptoms_model import Symptoms
from ..database.models.disease_model import disease
from ..schemas.symptoms_schema import CreateSymptoms, UpdateSymptoms
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional, List


class CRUDSymptoms(CRUDBase[Symptoms, CreateSymptoms, UpdateSymptoms]):

    def get_id_by_name(self, db: Session, name: str) -> int:
        result = db.query(self.model).filter_by(name=name).first()
        return result.id

    def get_disease_filtered(self, db: Session, all_name: List[str]) -> List[disease]:
        symptoms_id = [self.get_id_by_name(db, name) for name in all_name]
        disease_filtered = db.query(disease).filter(disease.symptoms.contains(symptoms_id)).all()
        return disease_filtered

    pass


symptoms = CRUDSymptoms(Symptoms)
