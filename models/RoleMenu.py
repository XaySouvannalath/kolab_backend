from typing import Union
from pydantic import BaseModel
from datetime import datetime

class RoleMenu(BaseModel):
    id: Union[int, None] = None
    role_id: int
    menu_id: int
    created_date: Union[datetime, None] = None
    created_by: Union[str, None] = None
    last_modified_date: Union[datetime, None] = None
