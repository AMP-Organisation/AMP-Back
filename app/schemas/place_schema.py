from typing import Optional, List

from pydantic import BaseModel


class PlaceBase(BaseModel):
    id: Optional[int]
    address: Optional[str]
    zip_code: Optional[str]
    department: Optional[str]
    region: Optional[str]
    country_code: Optional[str]
    type_id: Optional[int]
    city: Optional[str]
    tags: Optional[List[int]]


class CreatePlace(PlaceBase):
    address: str
    zip_code: str
    department: str
    region: str
    type_id: int
    city: str
    tags: Optional[List[int]]


class UpdatePlace(PlaceBase):
    id: int
    pass


class DeletePlace(BaseModel):
    id: int
    pass


class GetPlace(BaseModel):
    id: Optional[int]
    address: Optional[str]
    department: Optional[str]
    city: Optional[str]
    pass


class PlaceResponse(PlaceBase):
    class Config:
        orm_mode = True
