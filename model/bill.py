from pydantic import BaseModel
from typing import Union, List

class BillService(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    price: Union[float, None] = None
    status: Union[int, None] = None
    note: Union[str, None] = None
    quantity: Union[int, None] = None

class BillInfo(BaseModel):
    title: Union[str, None] = None
    list_service: Union[List[BillService], None] = None
    total: Union[int, None] = None
    paid: Union[int, None] = None
    loan: Union[int, None] = None
    note: Union[str, None] = None

class Bill(BaseModel):
    id: Union[int, None] = None
    id_apartment: Union[int, None] = None
    info: Union[BillInfo, None] = None
    time_create: Union[str, None] = None