from ..crud.crud_base import CRUDBase
from ..database.models.place_model import place, place_type, place_tags
from ..schemas.place_schema import CreatePlace, UpdatePlace
from sqlalchemy.orm import Session
from sqlalchemy_filters import apply_filters
from typing import Optional, List


class CRUDPlace(CRUDBase[place, CreatePlace, UpdatePlace]):

    def get_by_address(self, db: Session, filters) -> List[Optional[place]]:
        filter_spec = []
        place_found = []
        names = 'address department city'.split()
        search_place = db.query(self.model)
        for name, filt in zip(names, filters):
            if filt is not None:
                filter_spec.append(
                    {'model': self.model.__tablename__, 'field': name, 'op': 'like', 'value': '%%' + filt + '%%'}
                )
        filtered_place = apply_filters(search_place, filter_spec)
        result = db.execute(filtered_place)

        for value in result:
            result = self.get(db, value[0])
            place_found.append(result)

        return place_found

    @staticmethod
    def get_type(db: Session, skip: int = 0, limit: int = 100) -> List[Optional[place_type]]:
        return db.query(place_type).offset(skip).limit(limit).all()

    def get_place_filtered(self, db: Session, id_place: int) -> List[Optional[place]]:
        return db.query(self.model).filter_by(type_id=id_place).all()

    @staticmethod
    def get_tags(db: Session, list_tags: List[int]) -> List[Optional[place_tags]]:
        result = []
        print(list_tags)
        for value in list_tags:
            current_value = db.query(place_tags).get(value)
            result.append(current_value)
        return result
    pass


place = CRUDPlace(place)
