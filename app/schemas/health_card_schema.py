from typing import Optional, List

from pydantic import BaseModel


class HealthCardBase(BaseModel):
    id: Optional[int]
    allergy: Optional[List[int]]
    blood_group: Optional[str]
    disease: Optional[List[int]]
    user_id: Optional[int]


class CreateHealthCard(HealthCardBase):
    allergy: Optional[List[object]]
    blood_group: Optional[object]
    disease: Optional[List[object]]
    user_id: Optional[int]

    class Config:
        arbitrary_types_allowed = True


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
