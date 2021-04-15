from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud.crud_health_card import crud_health_card
from ..database.models.health_card_model import health_card
from ..schemas import health_card_schema, message

health_card_router = APIRouter(
    prefix='/health_card'
)


@health_card_router.post('/', response_model=health_card_schema.HealthCardResponse)
def user_health_card(*, db: Session = Depends(get_db), health_card_in: health_card_schema.GetHealthCard) -> health_card:
    current_user = crud_health_card.get_by_user(db, health_card_in.user_id)
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user do not exist in the system.",
        )
    return current_user


@health_card_router.delete('/deleteInformations', response_model=message.Message)
def user_health_card(*, db: Session = Depends(get_db), health_card_in: health_card_schema.GetHealthCard) -> Dict[
    str, str]:
    current_user = crud_health_card.get_by_user(db, user_id=health_card_in.user_id)

    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user was not deleted.",
        )
    crud_health_card.remove(db, model_id=current_user.id)
    return {"message": "User informations have been deleted."}
