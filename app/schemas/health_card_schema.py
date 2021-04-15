from typing import Optional, List

from pydantic import BaseModel


class HealthCardBase(BaseModel):
    id: Optional[int]
    allergy: Optional[List[int]]
    blood_group: Optional[str]
    disease: Optional[List[int]]
    user_id: Optional[int]


class CreateHealthCard(HealthCardBase):
    allergy: Optional[List[int]]
    blood_group: Optional[str]
    disease: Optional[List[int]]
    user_id: Optional[int]


class UpdateHealthCard(HealthCardBase):
    id: int
    pass


class DeleteHealthCard(BaseModel):
    id: int
    pass


class GetHealthCard(BaseModel):
    user_id: int


class HealthCardResponse(HealthCardBase):
    class Config:
        orm_mode = True
