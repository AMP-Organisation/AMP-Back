from pydantic import BaseModel
from typing import Optional, List


class disease(BaseModel):
    id: Optional[int]

# a specific schema for patch a disease
class diseasePatch(disease):
    name: Optional[str]
    description: Optional[str]
    is_vaccine: Optional[bool]
    is_treatment: Optional[bool]
    danger_level: Optional[int]

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