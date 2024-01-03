from pydantic import BaseModel
from typing import Union

class PairApartmentPeople(BaseModel):
    id_apartment: Union[int, None] = None
    id_people: Union[int, None] = None