from pydantic import BaseModel
import datetime


class ShowUser(BaseModel):
    """
       This is the description of the main model
    """
    last_name: str
    first_name: str
    email: str
    username: str
    age: int
    dt_inscription: datetime.datetime

    class Config:
        orm_mode = True
