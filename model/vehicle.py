from pydantic import BaseModel
from typing import Union, List

class VehicleInfo(BaseModel):
    status: Union[int, None] = None
    note: Union[str, None] = None
    apartment_name: Union[str, None] = None

class Vehicle(BaseModel):
    id: Union[int, None] = None
    id_apartment: Union[int, None] = None
    name: Union[str, None] = None
    info: Union[VehicleInfo, None] = None