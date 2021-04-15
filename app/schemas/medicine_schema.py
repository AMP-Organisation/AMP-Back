from typing import Optional

from pydantic import BaseModel


class PrincipleActive(BaseModel):
    id: Optional[int]
    name: Optional[str]


class CreatePrincipleActive(PrincipleActive):
    name: str
    max_dose_mg: int


class UpdatePrincipleActive(PrincipleActive):
    id: int


class PrincipleActiveResponse(PrincipleActive):
    class Config:
        orm_mode = True
