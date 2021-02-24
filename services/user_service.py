from sqlalchemy.orm import Session
from models import models
from fastapi import HTTPException, status


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User with the id {id} is not available")
    return user
