from typing import Optional, List
from pydantic import BaseModel
import datetime


class TreatmentBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    medicine_id: Optional[List[int]]
    beginning_date: Optional[datetime.datetime]
    ending_date: Optional[datetime.datetime]
    user_id: Optional[int]


class CreateTreatment(TreatmentBase):
    name: str
    description: str
    medicine_id: Optional[List[int]]
    beginning_date: Optional[datetime.datetime]
    ending_date: Optional[datetime.datetime]


class GetTreatments(TreatmentBase):
    all_treatment: List[int]


class GetTreatment(TreatmentBase):
    current_treatment: int


class UpdateTreatment(TreatmentBase):
    id: int


class DeleteMedicineFromTreatment(BaseModel):
    id: int
    medicine_id: int


class TreatmentResponse(TreatmentBase):
    class Config:
        orm_mode = True
