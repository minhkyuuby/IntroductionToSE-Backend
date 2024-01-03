from pydantic import BaseModel
from typing import Union

class InfoApartment(BaseModel):
    status: Union[int, None] = None
    note: Union[str, None] = None
    area: Union[float, None] = None

class Apartment(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    info: Union[InfoApartment, None] = None