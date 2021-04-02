from typing import Optional

from pydantic import BaseModel


class Place_type(BaseModel):
    id: Optional[int]
    type: Optional[str]


class PlaceResponse(Place_type):
    class Config:
        orm_mode = True
