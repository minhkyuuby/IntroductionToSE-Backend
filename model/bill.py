from pydantic import BaseModel
from typing import Union, List

class BillService(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    price: Union[float, None] = None
    status: Union[int, None] = None
    note: Union[str, None] = None

class BillInfo(BaseModel):
    list_service: Union[List[BillService], None] = None
    note: Union[str, None] = None

class Bill(BaseModel):
    id: Union[int, None] = None
    id_apartment: Union[int, None] = None
    info: Union[BillInfo, None] = None
    time_create: Union[str, None] = None