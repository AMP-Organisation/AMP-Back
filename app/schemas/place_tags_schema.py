from typing import Optional, List

from pydantic import BaseModel


class Place_tags(BaseModel):
    id: Optional[int]
    tags: str


class GetTags(Place_tags):
    tags: List[int]


class PlaceTagResponse(Place_tags):
    class Config:
        orm_mode = True
