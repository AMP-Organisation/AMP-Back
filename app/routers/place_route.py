from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud import crud_place
from ..schemas import place_schema, place_type_schema, place_tags_schema

place_router = APIRouter(
    prefix='/place'
)


@place_router.post('/getServices', response_model=List[place_tags_schema.PlaceTagResponse])
def show_place_service(*, db: Session = Depends(get_db), place_in: place_tags_schema.GetTags):
    place_found = crud_place.place.get_tags(db, place_in.tags)
    return place_found


@place_router.get('/getAll', response_model=List[place_schema.PlaceResponse])
def show_all_place(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    :return: all place in database
    """
    all_place = crud_place.place.get_multi(db, skip=skip, limit=limit)
    return all_place


@place_router.post('/getPlace', response_model=place_schema.PlaceResponse)
def show_all_place(*, db: Session = Depends(get_db), place_in: place_schema.GetPlace) -> Any:
    """
    :return: current place in database
    """
    current_place = crud_place.place.get(db, place_in.id)
    return current_place


@place_router.get('/type_place', response_model=List[place_type_schema.PlaceResponse])
def show_type_place(db: Session = Depends(get_db)) -> Any:
    type_place = crud_place.place.get_type(db)
    return type_place


@place_router.post('/get_a_place', response_model=List[place_schema.PlaceResponse])
def show_place_wanted(*, db: Session = Depends(get_db), place_in: place_schema.GetPlace):
    filters = (place_in.address, place_in.department, place_in.city)
    print(filters)
    place_found = crud_place.place.get_by_address(db, filters)
    return place_found


@place_router.get('/filter_type/{id_place}', response_model=List[place_schema.PlaceResponse])
def show_place_filtered(id_place: int, db: Session = Depends(get_db)) -> Any:
    """
    :param id_place: the id of the type of place
    :param db: actual db session
    :return: a list of place filtered
    """
    print(id_place)
    place_filtered = crud_place.place.get_place_filtered(db, id_place)
    return place_filtered


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
