from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class RoleMenu(BaseModel):
    id: Optional[int]
    role_id: int
    menu_id: int
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
