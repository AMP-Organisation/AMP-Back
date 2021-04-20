from sqlalchemy.orm import Session

from ..crud.crud_base import CRUDBase
from ..database.models.health_card_model import health_card
from ..schemas.health_card_schema import CreateHealthCard, UpdateHealthCard


class CRUDUser(CRUDBase[health_card, CreateHealthCard, UpdateHealthCard]):

    def get_by_user(self, db: Session, user_id: int) -> health_card:
        result = db.query(self.model).filter_by(user_id=user_id).first()
        return result

    def delete(self, db: Session, user_id: int):
        current_health_card = self.get_by_user(db, user_id)
        self.remove(db=db, model_id=current_health_card.id)

    pass


crud_health_card = CRUDUser(health_card)
