from pydantic import BaseModel
from typing import Any, Union

class TemporaryCardInfo(BaseModel):
    note: Union[str, None] = None

class TemporaryCard(BaseModel):
    id: Union[int, None] = None
    id_people: Union[int, None] = None
    start: Union[str, None] = None
    end: Union[str, None] = None
    info: Union[TemporaryCardInfo, None] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "id_people": 1,
                    "start": "2021-01-01 00:00:00",
                    "end": "2021-01-01 00:00:00",
                    "info": {
                        "note": "Temporary card"
                    }
                }
            ]
        }
    }