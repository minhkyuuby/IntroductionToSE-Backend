from pydantic import BaseModel
from typing import Union

class ServiceCalculate(BaseModel):
    eval_price: Union[str, None] = None
    values: Union[dict, None] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "eval_price": "{area} * 1000",
                "values": {
                    "area": 100
                }
            }
        }
    }
    
    def run_price(self):
        try:
            return str(eval(self.eval_price.format(**self.values)))
        except:
            return "Invalid eval_price"

class ServiceInfo(BaseModel):
    eval_price: Union[str, None] = None
    status: Union[int, None] = None
    price: Union[int, None] = None
    unit: Union[str, None] = None
    note: Union[str, None] = None

class Service(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    info: Union[ServiceInfo, None] = None