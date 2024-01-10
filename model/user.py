from pydantic import BaseModel
from typing import Union

class UserInfo(BaseModel):
    name: Union[str, None] = None

class User(BaseModel):
    id: Union[int, None] = None
    username: Union[str, None] = None
    password: Union[str, None] = None
    info: Union[UserInfo, None] = None

class UserLogin(BaseModel):
    username: Union[str, None] = None
    password: Union[str, None] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "admin",
                    "password": "123456"
                }
            ]
        }
    }

class UserChangePassword(BaseModel):
    old_password: Union[str, None] = None
    new_password: Union[str, None] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "old_password": "123456",
                    "new_password": "654321"
                }
            ]
        }
    }