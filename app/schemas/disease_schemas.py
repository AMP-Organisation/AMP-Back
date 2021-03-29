from pydantic import BaseModel
from typing import Optional, List


class disease(BaseModel):
    id: Optional[int]

class baseDisease(disease):
    name: str
    description: str
    is_vaccine: bool

class moreDisease(baseDisease):
    is_treatment: bool
    danger_level: int

class typeDisease(BaseModel):
    id: Optional[int]
    type: str