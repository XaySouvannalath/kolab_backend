from typing import Union
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: Union[int, None] = None
    username: str
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    password: str
    is_active: Union[bool, None] = True
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
    user_role_id: Union[int, None] = None




class PasswordReset(BaseModel):
    username: str
    new_password: str