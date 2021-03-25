from ..crud.crud_base import CRUDBase
from ..database.models.place_model import place
from ..schemas.place_schema import CreatePlace, UpdatePlace
from sqlalchemy.orm import Session
from sqlalchemy_filters import apply_filters
from typing import Optional, List


class CRUDMedicine(CRUDBase[place, CreatePlace, UpdatePlace]):

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

    pass


place = CRUDMedicine(place)
