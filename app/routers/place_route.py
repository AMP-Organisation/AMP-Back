from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud import crud_place
from ..schemas import place_schema, message_schema

place_router = APIRouter(
    prefix='/place'
)


@place_router.get('/getAll', response_model=List[place_schema.PlaceResponse])
def show_all_place(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    :return: all place in database
    """

    all_place = crud_place.place.get_multi(db, skip=skip, limit=limit)
    return all_place


@place_router.post('/get_a_place', response_model=List[place_schema.PlaceResponse])
def show_place_wanted(*, db: Session = Depends(get_db), place_in: place_schema.GetPlace):
    result = ""
    filters = (place_in.address, place_in.department, place_in.city)
    print(filters)
    place_found = crud_place.place.get_by_address(db, filters)
    return place_found


@place_router.post('/add_a_place', response_model=place_schema.PlaceResponse)
def show_place_wanted(*, db: Session = Depends(get_db), place_in: place_schema.CreatePlace):
    print(place_in.city)
    filters = (place_in.department, place_in.city)
    print(filters)
    place = crud_place.place.get_by_address(db, place_in.address, filters)
    if place:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"A place already exist in the system with that address : "
                   f"{place_in.address + ', ' + place_in.city}",
        )
    else:
        new_place = crud_place.place.create(db, obj_in=place_in)
    return new_place
