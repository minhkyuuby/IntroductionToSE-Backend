from pydantic import BaseModel
from typing import Union

class InfoPeople(BaseModel):
    fullname: Union[str, None] = None
    phone_number: Union[str, None] = None
    identity: Union[str, None] = None
    cccd: Union[str, None] = None
    residentId: Union[str, None] = None
    birthdayResident: Union[str, None] = None

class People(BaseModel):
    id: Union[int, None] = None
    info: Union[InfoPeople, None] = None