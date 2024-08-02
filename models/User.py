from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: Optional[int]
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    password: str
    is_active: Optional[bool] = True
    created_date: Optional[datetime]
    created_by: Optional[str]
    last_modified_date: Optional[datetime]
