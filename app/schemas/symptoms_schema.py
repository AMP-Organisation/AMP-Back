from typing import Optional, List

from pydantic import BaseModel


class SymptomsBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    danger: Optional[int]


class CreateSymptoms(SymptomsBase):
    name: str
    danger: int


class UpdateSymptoms(SymptomsBase):
    id: int
    pass


class DeleteSymptoms(BaseModel):
    id: int
    pass


class GetSymptoms(BaseModel):
    all_name: Optional[List[str]]
    pass


class SymptomsResponse(SymptomsBase):
    class Config:
        orm_mode = True
