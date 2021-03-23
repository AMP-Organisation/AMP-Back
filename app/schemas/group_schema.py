from typing import Optional

from pydantic import BaseModel


class GroupBase(BaseModel):
    id: Optional[int]
    Type: str
    pass


class GroupResponse(GroupBase):
    class Config:
        orm_mode = True
